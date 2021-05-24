import sys
import json
import requests
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI client for heart disease prediction.")
    parser.add_argument("host", help="hostname for api request")
    parser.add_argument("-age", help="age (range 0 - 150)", default="75")
    parser.add_argument("-chol", help="cholesterol level(range 0 - 1000)", default="500")
    parser.add_argument("-sex", help="gender ('m' or 'f')", default="m")
    args = parser.parse_args()

    url = f'http://{args.host}/predict/'
    payload = {'sex': args.sex, 'age': args.age, 'chol': args.chol}

    r = requests.post(url, data=json.dumps(payload))

    if r.status_code == 200:
        diagnosis = "Healthy" if r.json()['target'] == '[1]' else "Sick"
        print(f"SEX:{args.sex} AGE:{args.age} CHOL:{args.chol} - {diagnosis}")
    else:
        print('status code:', r.status_code)
        for msg in r.json()['detail']:
            print(f"{msg['type']}:{msg['loc'][1]}:{msg['msg']}")
