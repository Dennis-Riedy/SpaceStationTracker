"""
Functionality to get weather details for specific 
location to determine if visibility for the user 
of the International Space Station.
"""

import os
import asyncio
import python_weather as pw

# TODO: Error handling around connections 
async def get_weather(location):
    """Retrieve weather information for specific location"""
    async with pw.Client() as client:
        weather = await client.get(location)

        print(weather.temperature)
        print(weather.visibility)
        print(weather.feels_like)

        for daily in weather.daily_forecasts:
            print(daily)

        for hourly in daily.hourly_forecasts:
            print(f'--> {hourly!r}')
            print(hourly.description)

if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(get_weather('Dublin'))
