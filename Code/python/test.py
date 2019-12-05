import requests
import os
from PIL import Image
from io import BytesIO
from time import perf_counter


def get_json(url):
    res = requests.get(url)
    return res.json()


def get_img_data(url):
    res = requests.get(url)
    return res.content


def save_img(data, file_path):
    with open(file_path, "wb") as file:
        file.write(data)


def fib(num):
	if num == 0 : 
		return 0
	if num == 1:
		return 1
	return fib(num - 1) + fib(num -2)


def save_results(text_path, **kwargs):
    with open(text_path, "a") as file:
        file.write("\n")
        for k,v in kwargs:
            file.writelines()


def get_baseurl(path):
    with open(path, "r") as file:
        return file.read()


def time_func(func, args, results, title):
    now = perf_counter()
    func(args)
    end = perf_counter() - now
    results[title] = end


def main():
    results = {}
    baseurl = get_baseurl("../../Text/url.txt")
    json = get_json(baseurl+"/json")
    num = json["num"]

    now = perf_counter()
    img_data = get_img_data(baseurl+"/img")
    results["download img"] = perf_counter() - now

    now = perf_counter()
    save_img(img_data, "img/img.jpg")
    results["saving img"] = perf_counter() - now

    now = perf_counter()
    fib(num)
    results["fib"] = perf_counter() - now

    save_results('../../Text/results.txt', **results)
    print(results)
    print("end")

main()