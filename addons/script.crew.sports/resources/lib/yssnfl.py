
import base64, codecs
thecrew = 'aW1wb3J0IHJlcXVlc3RzDQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cA0KaW1wb3J0IHJlDQppbXBvcnQgYmFzZTY0DQojOTQ1NDgNCmdhbWUgPSBbXQ0KDQpkZWYgZ2V0X2dhbWVzKCk6DQogICAgdXJsID0gImh0dHA6Ly95b3Vyc3BvcnRzLnN0cmVhbS8iDQogICAgYWdlbnQgPSAiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzc5LjAuMzk0NS4xMTcgU2FmYXJpLzUzNy4zNiINCiAgICBodG1sQ29udGVudCA9IHJlcXVlc3RzLmdldCh1cmwsaGVhZGVycz17InVzZXItYWdlbnQiOmFnZW50fSkuY29udGVudA0KICAgIHNvdXAgPSBCZWF1dGlmdWxTb3VwKGh0bWxDb250ZW50LCAnaHRtbC5wYXJzZXInKQ0KICAgIG5jYWFiID0gc291cC5zZWxlY3QoIiNuZmwiKQ0KICAgIGlmIG5jYWFiOg0KICAgICAgICBkaXZzID0gbmNhYWJbMF0uc2VsZWN0KCIuY29sLTEyLnczLXRleHQtd2hpdGUudzMtc21hbGwiKQ0KICAgICAgICBmb3IgZGl2IGluIGRpdnM6DQogICAgICAgICAgICB0aXRsZSA9IGRpdi5zZWxlY3QoIi53My1jZW50ZXIiKVswXS50ZXh0LnN0cmlwKCkNCiAgICAgICAgICAgIGxpbmtzID0gZGl2LnNlbGVjdCgiYSIpDQogICAgICAgICAgICBmb3IgbGluayBpbiBsaW5rczoNCiAgICAgICAgICAgICAgICBpZiAoIj92PW5mbCIgbm90IGluIGxpbmtbJ2hyZWYnXS5lbmNvZGUoImFzY2lpIikpOg0KICAgICAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICAgICAgICAgIGVsc2U6DQogICAgICAgICAgICAgICAgICAgIHVybCA9IGxpbmtbJ2hyZWYnXQ0KDQogICAgICAgICAgICAgICAgICAgIGlmICJodHRwIiBub3QgaW4gdXJsOg0KICAgICAgICAgICAgICAgICAgICAgICAgdXJsID0gImh0dHA6Ly95b3Vyc3BvcnRzLnN0cmVhbSIgKyB1cmwNCiAgICAgICAgICAgICAgICAgICAgICAgIGdhbWUuYXBwZW5kKHsidGl0bGUiOnRpdGxlLmVuY29kZSgiYXNjaWkiKSwibGluayI6dXJsLmVuY29kZSgiYXNjaWkiKX0pDQogICAgICAgICAgICAgICAgI'
doesnt = 'PNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjLKAmQDbtVPNtVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNAPvNtVPNtVPNtQDbtVPNtMJkmMGbAPvNtVPNtVPNtpTSmpj0XQDbtVPNtpzI0qKWhVTquoJHAPt0XQDbAPaA0pzIuoFN9VSgqQDcxMJLtM2I0K3A0pzIuoFufnJ5eXGbAPvNtVPOhnTkHo2gyovN9VUWypKIyp3EmYzqyqPtanUE0pUZ6Yl9vnKEvqJAeMKDho3WaY3EbpzI3Y3EyrUEznJkypl9lLKpioJSmqTIlY25boP50rUDaXF5wo250MJ50QDbtVPNtozufK2S1qTttCFNvsRAio2gcMG1OqKEbo3WcrzS0nJ9hCFVtXlOhnTkHo2gyot0XVPNtVPZ8nJMlLJ1yVTMlLJ1yLz9lMTIlCGNtnTIcM2u0CGRjZPHtq2yxqTt9ZGNjWFOmpzZ9QDbtVPNtLJqyoaDtCFNvGJ96nJkfLF81YwNtXSqcozEiq3ZtGyDtZGNhZQftI2yhAwD7VUt2APxtDKOjoTIKMJWYnKDiAGZ3YwZ2VPuYFSEAGPjtoTyeMFOUMJAeolxtD2ulo21yYmp5YwNhZmx0AF4kZGptH2SzLKWcYmHmAl4mAvVAPvNtVPObqT1fD29hqTIhqPN9VUWypKIyp3EmYzqyqPufnJ5eYTuyLJEypaZ9rlW1p2IlYJSaMJ50VwcuM2IhqU0cYzAioaEyoaDAPvNtVPOmo3IjVQ0tDzIuqKEcMaIfH291pPubqT1fD29hqTIhqPjtW2u0oJjhpTSlp2IlWlxAPvNtVPNwpUWcoaDbp291pP5jpzI0qTyzrFxAPvNtVPOcMaWuoJHtCFOlMF5wo21jnJkyXPp8nJMlLJ1yVTSfoT93MaIfoUAwpzIyow0vVvOuoTkiq3ElLJ5mpTSlMJ5wrG0vVvOzpzSgMJWipzEypw0vZPVtnTIcM2u0CFVkZQNyVvOmL3WioTkcozp9Vz5iVvOmpzZ9VvthXm8cVvpfpzHhER9HDHkZXF5znJ5xLJkfXUA0pvumo3IjYaOlMKE0nJM5XFxAPvNtVPOcMvOcMaWuoJH6QDbtVPNtVPNtVTyzpzSgMFN9VTyzpzSgMIfjKD0XVPNtVPNtVPObqT1fD29hqTIhqPN9VUWypKIyp3EmYzqyqPucMaWuoJHfnTIuMTIlpm17VaImMKVgLJqyoaDvBzSaMJ50YPWlMJMypzIlVwcfnJ5esFxhL29hqTIhqN0XVPNtVPNtVPNwpUWcoaDbnUEgoRAioaEyoaDcQDbtVPNtVPNtVUAiqKNtCFOPMJS1qTyzqJkGo3IjXTu0oJkQo250MJ50YPqbqT1fYaOupaAypvpcQDbtVPNtVPNtVT'
do = 'NvbnRlbnQgPSBzdHIoc291cC5wcmV0dGlmeSkNCiAgICAgICAgI2NvbnRlbnQgPSBjb250ZW50LnJlcGxhY2UoImF0b2IoJyIsIiIpDQogICAgICAgICNwcmludChjb250ZW50KQ0KICAgICAgICBlbmNyeXB0ID0gcmUuY29tcGlsZSgiYXRvYlwoLis/XCkiLHJlLkRPVEFMTCkuZmluZGFsbChjb250ZW50KQ0KICAgICAgICAjcHJpbnQoZW5jcnlwdCkNCiAgICAgICAgaWYgZW5jcnlwdDoNCiAgICAgICAgICAgIGVuY3J5cHQgPSBlbmNyeXB0WzBdDQogICAgICAgICAgICBlbmNyeXB0ID0gZW5jcnlwdC5yZXBsYWNlKCJhdG9iKCciLCIiKS5yZXBsYWNlKCInKSIsIiIpDQogICAgICAgICAgICAjYXRvYkkgPSBlbmNyeXB0LmZpbmQoImF0b2IiKQ0KICAgICAgICAgICAgI2VuY3J5cHQgPSBlbmNyeXB0WzphdG9iSV0NCiAgICAgICAgICAgIA0KICAgICAgICAgICAgI3ByaW50KGVuY3J5cHQpDQogICAgICAgICAgICBkZWNyeXB0ID0gYmFzZTY0LmI2NGRlY29kZShlbmNyeXB0KQ0KICAgICAgICAgICAgI3ByaW50KGRlY3J5cHQpDQogICAgICAgICAgICAjcHJpbnQoIkZvdW5kIElUIikNCiAgICAgICAgICAgIHN0cmVhbS5hcHBlbmQoeyJ0aXRsZSI6InN0cmVhbSIsImxpbmsiOmRlY3J5cHQgKyAifFJlZmVyZXI9IiArIGlmcmFtZX0pDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICBwYXNzDQogICAgZWxzZToNCiAgICAgICAgaWZyYW1lID0gc291cC5zZWxlY3QoIiNwbGF5ZXIiKQ0KICAgICAgICBpZiBpZnJhbWU6DQogICAgICAgICAgICBpZnJhbWUgPSBpZnJhbWVbMF1bJ3NyYyddDQogICAgICAgICAgICBpZiAiaHR0cCIgbm90IGluIGlmcmFtZToNCiAgICAgICAgICAgICAgICBpZnJhbWUgPSAiaHR0cDovL3lvdXJzcG9ydHMuc3RyZWFtLyIgKyBpZnJhbWUNCiAgICAgICAgICAgIGh0bWxDb250ZW50ID0gcmVxdWVzdHMuZ2V0KGlmcmFtZSxoZWFkZXJzPXsidXNlci1hZ2VudCI6YWdlbnQsInJlZmVyZXIiOmxpbmt9KS5jb250ZW50DQogICAgICAgICAgICAjcHJpbnQoaHRtbENvbnRlbnQpDQogICAgICAgICAgICBzb3VwID0gQmVhdXRpZnVsU291cChodG1sQ29udGV'
drama = 'hqPjanUEgoP5jLKWmMKVaXD0XVPNtVPNtVPNtVPNtL29hqTIhqPN9VUA0pvumo3IjYaOlMKE0nJM5XD0XVPNtVPNtVPNtVPNtV2AioaEyoaDtCFOwo250MJ50YaWypTkuL2HbVzS0o2VbWlVfVvVcQDbtVPNtVPNtVPNtVPNwpUWcoaDbL29hqTIhqPxAPvNtVPNtVPNtVPNtVTIhL3W5pUDtCFOlMF5wo21jnJkyXPWuqT9vKPthXm9pXFVfpzHhER9HDHkZXF5znJ5xLJkfXTAioaEyoaDcQDbtVPNtVPNtVPNtVPNwpUWcoaDbMJ5wpayjqPxAPvNtVPNtVPNtVPNtVTyzVTIhL3W5pUD6QDbtVPNtVPNtVPNtVPNtVPNtMJ5wpayjqPN9VTIhL3W5pUEoZS0APvNtVPNtVPNtVPNtVPNtVPOyozAlrKO0VQ0tMJ5wpayjqP5lMKOfLJAyXPWuqT9vXPpvYPVvXF5lMKOfLJAyXPVaXFVfVvVcQDbtVPNtVPNtVPNtVPNtVPNtV2S0o2WWVQ0tMJ5wpayjqP5znJ5xXPWuqT9vVvxAPvNtVPNtVPNtVPNtVPNtVPNwMJ5wpayjqPN9VTIhL3W5pUEoBzS0o2WWKD0XVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPNtVPNtVPNtVPAjpzyhqPuyozAlrKO0XD0XVPNtVPNtVPNtVPNtVPNtVTEyL3W5pUDtCFOvLKAyAwDhLwL0MTIwo2EyXTIhL3W5pUDcQDbtVPNtVPNtVPNtVPNtVPNtMTIwpayjqPN9VTEyL3W5pUDhMJ5wo2EyXPWup2AcnFVcQDbtVPNtVPNtVPNtVPNtVPNtMTIwpayjqPN9VTEyL3W5pUDtXlNvsSWyMzIlMKV9VvNeVTyzpzSgMD0XVPNtVPNtVPNtVPNtVPNtVPAjpzyhqPuxMJAlrKO0XD0XVPNtVPNtVPNtVPNtVPNtVPAjpzyhqPtvEz91ozDtFIDvXD0XVPNtVPNtVPNtVPNtVPNtVUA0pzIuoF5upUOyozDbrlW0nKEfMFV6VaA0pzIuoFVfVzkcozfvBzEyL3W5pUDhMJ5wo2EyXPWup2AcnFVcsFxAPvNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtpTSmpj0XVPNtVPNtVPNtVPNtVPNtVN0XVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtpTSmpj0XVPNtVPNtVPNAPt0XVPNtVUWyqUIlovOmqUWyLJ0APvNtVPNAPvNtVPNAPvAjpzyhqPuaMKEsM2SgMKZbXFxAPvAjpzyhqPuaMKEsp3ElMJSgXPWbqUEjBv8irJ91paAjo3W0pl5mqUWyLJ0ioTy2MG92CJ5vLG9aCKWupUEipaZvXFxAPt=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))