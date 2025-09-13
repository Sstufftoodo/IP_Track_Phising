#!/usr/bin/python
import time as t
import os
import requests as req
import colorama
import pyfiglet
from colorama import *
from flask import Flask, render_template

app = Flask(__name__)

def get_info(ip_address):
    balasan = req.get(f"https://ipapi.co/{ip_address}/json/").json()
    location_data = {
        "Ip Address": ip_address,
        "city": balasan.get("city"),
        "region": balasan.get("region"),
        "country": balasan.get("country_name"),
        "Ip Address Type": balasan.get("version"),
        "Region Code": balasan.get("region_code"),
        "Postal Code": balasan.get("postal"),
        "Latitude": balasan.get("latitude"),
        "Longitude": balasan.get("longitude"),
        "TimeZone": balasan.get("timezone"),
        "Country code": balasan.get("country_calling_code"),
        "Currency": balasan.get("currency"),
        "Currency Name": balasan.get("currency_name"),
        "Languages": balasan.get("languages"),
        "Country Area": balasan.get("country_area"),
        "Population": balasan.get("country_population"),
        "ASN": balasan.get("asn"),
        "Organization": balasan.get("org")
    }
    
    lat = str(balasan.get("latitude"))
    long = str(balasan.get("longitude"))
    embed_url = f"https://www.google.com/maps?q={lat},{long}&hl=es;z=14&output=embed"
    return location_data, embed_url

@app.route("/")
def index():
    ip = req.get("https://icanhazip.com").text.strip()
    location_data, embed_url = get_info(ip)
    return render_template("testing.html", location=location_data, map_url=embed_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)