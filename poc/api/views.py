from django.shortcuts import render
from django.http import HttpResponse
import asyncio

async def index(request):
    seconds_to_sleep = 10
    await asyncio.sleep(seconds_to_sleep)
    return HttpResponse(f"Sleeped by {seconds_to_sleep} seconds.")

# def index(request):
#     seconds_to_sleep = 10
#     asyncio.sleep(seconds_to_sleep)
#     return HttpResponse(f"Sleeped by {seconds_to_sleep} seconds.")
