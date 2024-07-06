from django.shortcuts import render
from .generateAccessToken import get_access_token
from .stkPush import initiate_stk_push

def get_access_token_view(request):
    return get_access_token(request)

def initiata_stk_push_view(request):
    return initiate_stk_push(request)