import streamlit as st
import websocket
import json
import requests

email = st.secrets.goober_dash_credentials.email
password = st.secrets.goober_dash_credentials.password


def refresh_token():
    data = {
        "email": email,
        "password": password,
        "vars": {
            "client_version": "99999",
        },
    }

    headers = {"authorization": "Basic OTAyaXViZGFmOWgyZTlocXBldzBmYjlhZWIzOTo="}

    try:
        response = requests.post(
            "https://gooberdash-api.winterpixel.io/v2/account/authenticate/email?create=false",
            data=json.dumps(data),
            headers=headers,
        )
        token = json.loads(response.content)["token"]
        return token
    except Exception:
        print("Invalid credentials!")


def list_levels():
    try:
        token = str(refresh_token())
        ws1 = websocket.create_connection(
            "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token=" + token
        )
        levels_query = {
            "cid": "6",
            "rpc": {"id": "levels_query_curated", "payload": "{}"},
        }
        ws1.send(json.dumps(levels_query).encode())
        ws1.recv()
        msg1 = ws1.recv()
        output = json.loads(msg1)
        ws1.close()
        output2 = json.loads(output["rpc"]["payload"])
        race_dict = {}

        for level in output2["levels"]:
            if level["game_mode"] == "Race":
                race_dict[level["id"]] = level["name"]
        return race_dict
    except Exception as e:
        print(e)


def fetch_leaderboard(level_id):
    none_return = True
    while none_return:
        try:
            token = str(refresh_token())

            ws2 = websocket.create_connection(
                "wss://gooberdash-api.winterpixel.io/ws?lang=en&status=true&token="
                + token
            )

            payload = '{"level_id":"' + str(level_id) + '","limit":10000}'
            query_leaderboard = {
                "cid": "999",
                "rpc": {
                    "id": "time_trial_query_leaderboard",
                    "payload": f"{payload}",
                },
            }
            ws2.send(json.dumps(query_leaderboard).encode())
            ws2.recv()
            recv = json.loads(ws2.recv())
            payload_recv = json.loads(recv["rpc"]["payload"])
            records = payload_recv["records"]
            if records is not None:
                none_return = False
            return records

        except Exception as e:
            print(e)
            pass