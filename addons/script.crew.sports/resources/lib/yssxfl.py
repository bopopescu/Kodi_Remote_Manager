
import base64, codecs
thecrew = 'aW1wb3J0IHJlcXVlc3RzDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KaW1wb3J0IHJlDQppbXBvcnQgYmFzZTY0DQojOTQ1NDkNCmdhbWUgPSBbXQ0KDQpkZWYgZ2V0X2dhbWVzKCk6DQogICAgdXJsID0gImh0dHA6Ly95b3Vyc3BvcnRzLnN0cmVhbS8iDQogICAgYWdlbnQgPSAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc5LjAuMzk0NS4xMTcgU2FmYXJpLzUzNy4zNiINCiAgICBodG1sQ29udGVudCA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz17InVzZXItYWdlbnQiOmFnZW50fSkuY29udGVudA0KICAgIHNvdXAgPSBCZWF1dGlmdWxTb3VwKGh0bWxDb250ZW50LCAnaHRtbC5wYXJzZXInKQ0KICAgIHhmbCA9IHNvdXAuc2VsZWN0KCIjbmZsIikNCiAgICBpZiB4Zmw6DQogICAgICAgIGRpdnMgPSB4ZmxbMF0uc2VsZWN0KCIuY29sLTEyLnczLXRleHQtd2hpdGUudzMtc21hbGwiKQ0KICAgICAgICBmb3IgZGl2IGluIGRpdnM6DQogICAgICAgICAgICB0aXRsZSA9IGRpdi5zZWxlY3QoIi53My1jZW50ZXIiKVswXS50ZXh0LnN0cmlwKCkNCiAgICAgICAgICAgIGxpbmtzID0gZGl2LnNlbGVjdCgiYSIpDQogICAgICAgICAgICBmb3IgbGluayBpbiBsaW5rczoNCiAgICAgICAgICAgICAgICBpZiAoImM9bmZsIiBub3QgaW4gbGlua1snaHJlZiddLmVuY29kZSgiYXNjaWkiKSk6DQogICAgICAgICAgICAgICAgICAgIGNvbnRpbnVlDQogICAgICAgICAgICAgICAgZWxzZToNCiAgICAgICAgICAgICAgICAgICAgdXJsID0gbGlua1snaHJlZiddDQoNCiAgICAgICAgICAgICAgICAgICAgaWYgImh0dHAiIG5vdCBpbiB1cmw6DQogICAgICAgICAgICAgICAgICAgICAgICB1cmwgPSAiaHR0cDovL3lvdXJzcG9ydHMuc3RyZWFtIiArIHVybA0KICAgICAgICAgICAgICAgICAgICAgICAgZ2FtZS5hcHBlbmQoeyJ0aXRsZSI6dGl0bGUuZW5jb2RlKCJhc2NpaSIpLCJsaW5rIjp1cmwuZW5jb2RlKCJhc2NpaSIpfSkNCiAgICAgICAgI'
doesnt = 'PNtVPNtVPNtVPNtMJkmMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtVPNtVPNtVPNtVPNtQDbtVPNtVPNtVN0XVPNtVPNtVPNAPvNtVPOyoUAyBt0XVPNtVPNtVPOjLKAmQDbAPvNtVPOlMKE1pz4tM2SgMD0XQDbAPt0Xp3ElMJSgVQ0tJ10APzEyMvOaMKEsp3ElMJSgXTkcozfcBt0XVPNtVT5boSEin2IhVQ0tpzIkqJImqUZhM2I0XPqbqUEjpmbiY2WcqTW1L2gyqP5ipzpiqTulMKpiqTI4qTMcoTImY3Wuql9gLKA0MKViozufYaE4qPpcYzAioaEyoaDAPvNtVPOhnTksLKI0nPN9VPW8D29in2yyCHS1qTuipzy6LKEco249VvNeVT5boSEin2IhQDbtVPNtVmkcMaWuoJHtMaWuoJIvo3WxMKV9ZPObMJyanUD9ZGNjWFO3nJE0nQ0kZQNyVUAlLm0APvNtVPOuM2IhqPN9VPWAo3ccoTkuYmHhZPNbI2yhMT93plOBIPNkZP4jBlOKnJ42AQftrQL0XFOOpUOfMIqyLxgcqP81ZmphZmLtXRgVIR1ZYPOfnJgyVRqyL2giXFOQnUWioJHiAmxhZP4mBGD1YwRkAlOGLJMupzxiAGZ3YwZ2Vt0XVPNtVTu0oJkQo250MJ50VQ0tpzIkqJImqUZhM2I0XTkcozffnTIuMTIlpm17VaImMKVgLJqyoaDvBzSaMJ50sFxhL29hqTIhqN0XVPNtVUAiqKNtCFOPMJS1qTyzqJkGo3IjXTu0oJkQo250MJ50YPNanUEgoP5jLKWmMKVaXD0XVPNtVPAjpzyhqPumo3IjYaOlMKE0nJM5XD0XVPNtVTyzpzSgMFN9VUWyYzAioKOcoTHbWmkcMaWuoJHtLJkfo3qzqJkfp2AlMJIhCFVvVTSfoT93qUWuoaAjLKWyozA5CFVvVTMlLJ1yLz9lMTIlCFVjVvObMJyanUD9VwRjZPHvVUAwpz9foTyhMm0voz8vVUAlLm0vXP4eClxvWlklMF5RG1EOGRjcYzMcozEuoTjbp3ElXUAiqKNhpUWyqUEcMaxcXD0XVPNtVTyzVTyzpzSgMGbAPvNtVPNtVPNtnJMlLJ1yVQ0tnJMlLJ1yJmOqQDbtVPNtVPNtVTu0oJkQo250MJ50VQ0tpzIkqJImqUZhM2I0XTyzpzSgMFkbMJSxMKWmCKfvqKAypv1uM2IhqPV6LJqyoaDfVaWyMzIlMKVvBzkcozg9XF5wo250MJ50QDbtVPNtVPNtVPAjpzyhqPubqT1fD29hqTIhqPxAPvNtVPNtVPNtp291pPN9VRWyLKI0nJM1oSAiqKNbnUEgoRAioaEyoaDfW2'
do = 'h0bWwucGFyc2VyJykNCiAgICAgICAgY29udGVudCA9IHN0cihzb3VwLnByZXR0aWZ5KQ0KICAgICAgICAjY29udGVudCA9IGNvbnRlbnQucmVwbGFjZSgiYXRvYignIiwiIikNCiAgICAgICAgI3ByaW50KGNvbnRlbnQpDQogICAgICAgIGVuY3J5cHQgPSByZS5jb21waWxlKCJhdG9iXCguKz9cKSIscmUuRE9UQUxMKS5maW5kYWxsKGNvbnRlbnQpDQogICAgICAgICNwcmludChlbmNyeXB0KQ0KICAgICAgICBpZiBlbmNyeXB0Og0KICAgICAgICAgICAgZW5jcnlwdCA9IGVuY3J5cHRbMF0NCiAgICAgICAgICAgIGVuY3J5cHQgPSBlbmNyeXB0LnJlcGxhY2UoImF0b2IoJyIsIiIpLnJlcGxhY2UoIicpIiwiIikNCiAgICAgICAgICAgICNhdG9iSSA9IGVuY3J5cHQuZmluZCgiYXRvYiIpDQogICAgICAgICAgICAjZW5jcnlwdCA9IGVuY3J5cHRbOmF0b2JJXQ0KICAgICAgICAgICAgDQogICAgICAgICAgICAjcHJpbnQoZW5jcnlwdCkNCiAgICAgICAgICAgIGRlY3J5cHQgPSBiYXNlNjQuYjY0ZGVjb2RlKGVuY3J5cHQpDQogICAgICAgICAgICAjcHJpbnQoZGVjcnlwdCkNCiAgICAgICAgICAgICNwcmludCgiRm91bmQgSVQiKQ0KICAgICAgICAgICAgc3RyZWFtLmFwcGVuZCh7InRpdGxlIjoic3RyZWFtIiwibGluayI6ZGVjcnlwdCArICJ8VXNlci1BZ2VudD0iICsgYWdlbnQgKyAiJlJlZmVyZXI9IiArIGlmcmFtZX0pDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICBwYXNzDQogICAgZWxzZToNCiAgICAgICAgaWZyYW1lID0gc291cC5zZWxlY3QoIiNwbGF5ZXIiKQ0KICAgICAgICBpZiBpZnJhbWU6DQogICAgICAgICAgICBpZnJhbWUgPSBpZnJhbWVbMF1bJ3NyYyddDQogICAgICAgICAgICBpZiAiaHR0cCIgbm90IGluIGlmcmFtZToNCiAgICAgICAgICAgICAgICBpZnJhbWUgPSAiaHR0cDovL3lvdXJzcG9ydHMuc3RyZWFtLyIgKyBpZnJhbWUNCiAgICAgICAgICAgIGh0bWxDb250ZW50ID0gcmVxdWVzdHMuZ2V0KGlmcmFtZSxoZWFkZXJzPXsidXNlci1hZ2VudCI6YWdlbnQsInJlZmVyZXIiOmxpbmt9KS5jb250ZW50DQogICAgICAgICAgICA'
drama = 'wpUWcoaDbnUEgoRAioaEyoaDcQDbtVPNtVPNtVPNtVPOmo3IjVQ0tDzIuqKEcMaIfH291pPubqT1fD29hqTIhqPjanUEgoP5jLKWmMKVaXD0XVPNtVPNtVPNtVPNtL29hqTIhqPN9VUA0pvumo3IjYaOlMKE0nJM5XD0XVPNtVPNtVPNtVPNtV2AioaEyoaDtCFOwo250MJ50YaWypTkuL2HbVzS0o2VbWlVfVvVcQDbtVPNtVPNtVPNtVPNwpUWcoaDbL29hqTIhqPxAPvNtVPNtVPNtVPNtVTIhL3W5pUDtCFOlMF5wo21jnJkyXPWuqT9vKPthXm9pXFVfpzHhER9HDHkZXF5znJ5xLJkfXTAioaEyoaDcQDbtVPNtVPNtVPNtVPNwpUWcoaDbMJ5wpayjqPxAPvNtVPNtVPNtVPNtVTyzVTIhL3W5pUD6QDbtVPNtVPNtVPNtVPNtVPNtMJ5wpayjqPN9VTIhL3W5pUEoZS0APvNtVPNtVPNtVPNtVPNtVPOyozAlrKO0VQ0tMJ5wpayjqP5lMKOfLJAyXPWuqT9vXPpvYPVvXF5lMKOfLJAyXPVaXFVfVvVcQDbtVPNtVPNtVPNtVPNtVPNtV2S0o2WWVQ0tMJ5wpayjqP5znJ5xXPWuqT9vVvxAPvNtVPNtVPNtVPNtVPNtVPNwMJ5wpayjqPN9VTIhL3W5pUEoBzS0o2WWKD0XVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPAjpzyhqPuyozAlrKO0XD0XVPNtVPNtVPNtVPNtVPNtVTEyL3W5pUDtCFOvLKAyAwDhLwL0MTIwo2EyXTIhL3W5pUDcQDbtVPNtVPNtVPNtVPNtVPNtMTIwpayjqPN9VTEyL3W5pUDhMJ5wo2EyXPWup2AcnFVcQDbtVPNtVPNtVPNtVPNtVPNtMTIwpayjqPN9VTEyL3W5pUDtXlNvsSImMKVgDJqyoaD9VvNeVTSaMJ50VPftVvMFMJMypzIlCFVtXlOcMaWuoJHAPvNtVPNtVPNtVPNtVPNtVPNwpUWcoaDbMTIwpayjqPxAPvNtVPNtVPNtVPNtVPNtVPNwpUWcoaDbVxMiqJ5xVRyHVvxAPvNtVPNtVPNtVPNtVPNtVPOmqUWyLJ0hLKOjMJ5xXUfvqTy0oTHvBvWmqUWyLJ0vYPWfnJ5eVwcxMJAlrKO0YzIhL29xMFtvLKAwnJxvXK0cQDbtVPNtVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtVPNtVPNtVPNAPvNtVPNtVPNtMJkmMGbAPvNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtQDbAPvNtVPOlMKE1pz4tp3ElMJSgQDb='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))