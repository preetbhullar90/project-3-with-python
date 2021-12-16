"""
import colorama, os,random,google-auth and gspread link with run.py.
"""
import os
import random
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("hangman_game")


def get_all_words():
    """
    This function is for to
    get all the words from the gspread sheet.
    """
    lists = SHEET.worksheet("words_List").get_all_values()
    for item in lists:
        word_list = item
        return word_list
