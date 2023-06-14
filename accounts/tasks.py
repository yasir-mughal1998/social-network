from celery import shared_task
import logging
import requests
from datetime import datetime
from ipstack import GeoLookup
from accounts.models import CustomUser
from django.conf import settings
from tenacity import retry, stop_after_attempt, wait_fixed


logger = logging.getLogger(__name__)


@retry(stop=stop_after_attempt(3), wait=wait_fixed(1))
def get_holidays(country_code, date_today):

    CALENDARIFIC_API_KEY = settings.CALENDARIFIC_API_KEY
    data = None

    try:
        url = f'https://calendarific.com/api/v2/holidays?api_key={CALENDARIFIC_API_KEY}&country={country_code}&year={date_today[:4]}&month={date_today[5:7]}&day={date_today[8:]}'
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(e)

    return data


def is_holiday(date, holidays):
    if holidays:
        for holiday in holidays:
            if date == holiday['date']['iso']:
                return True
    return False


@shared_task(max_retries=3)
def process_signup(user_id, ip_address):

    logger.info("start process_signup.request retries retry count %s" %
                process_signup.request.retries)

    user = CustomUser.objects.get(id=user_id)

    IPSTACK_API_KEY = settings.IPSTACK_API_KEY

    try:
        geo_lookup = GeoLookup(IPSTACK_API_KEY)
    except Exception as e:
        print(e)

    location = None
    is_signup_date_holiday = False

    try:
        location = geo_lookup.get_location(ip_address)
        if location is None:
            print("Failed to find location.")
    except Exception as e:
        print(e)

    date_today = datetime.now().strftime('%Y-%m-%d')

    if location:
        holidays_data = get_holidays(location.get('country_code'), date_today)
        holidays = holidays_data['response']['holidays']
        is_signup_date_holiday = is_holiday(date_today, holidays)

    if is_signup_date_holiday:
        # Saving geolocation response and holiday API response to the user table
        user.geolocation = location
        user.holiday = holidays_data
        user.save()
        print("saved to user table")
    else:
        print("no data found")

    logger.info("end process_signup.request retries retry count %s" %
                process_signup.request.retries)
