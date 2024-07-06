from django.shortcuts import render
from .generateAccessToken import get_access_token
import requests
import json
from django.http import JsonResponse