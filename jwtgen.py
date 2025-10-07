Skip to content
wasdark336-7621's projects
wasdark336-7621's projects

Hobby

darkkk

BPe5Uk46T



Find…
F

Source
Output
jwtgen.py

        url = "https://loginbp.common.ggbluefox.com/MajorLogin"
        headers = {
            'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
            'Connection': "Keep-Alive",
            'Accept-Encoding': "gzip",
            'Content-Type': "application/octet-stream",
            'Expect': "100-continue",
            'X-Unity-Version': "2018.4.11f1",
            'X-GA': "v1 1",
            'ReleaseVersion': "OB50"
        }

        response = requests.post(url, data=bytes.fromhex(edata), headers=headers, verify=False)

        if response.status_code == 200:
            example_msg = output_pb2.Garena_420()
            try:
                example_msg.ParseFromString(response.content)
                response_dict = parse_response(str(example_msg))
                return jsonify({
                    "uid": uid,
                    "status": response_dict.get("status", "N/A"),
                    "token": response_dict.get("token", "N/A")
                })
            except Exception as e:
                return jsonify({
                    "uid": uid,
                    "error": f"Failed to deserialize the response: {str(e)}"
                }), 400
        else:
            return jsonify({
                "uid": uid,
                "error": f"Failed to get response: HTTP {response.status_code}, {response.reason}"
            }), 400
    except Exception as e:
        return jsonify({
            "uid": uid,
            "error": f"Internal error occurred: {str(e)}"
        }), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
darkkk – Deployment Source – Vercel
