
import base64, codecs
thecrew = 'aW1wb3J0IHJlcXVlc3RzDQppbXBvcnQgcmUNCmZyb20gYnM0IGltcG9ydCBCZWF1dGlmdWxTb3VwDQppbXBvcnQgeGJtY2d1aQ0KDQphZ2VudCA9ICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjE7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS83Ni4wLjM4MDkuMTMyIFNhZmFyaS81MzcuMzYnDQp1X2xpbmsgPSAnaHR0cDovLzZzdHJlYW0ueHl6L25obC1zdHJlYW1zLycNCm5obFRva2VuID0gcmVxdWVzdHMuZ2V0KCdodHRwczovL2JpdGJ1Y2tldC5vcmcvdGhyZXcvdGV4dGZpbGVzL3Jhdy9tYXN0ZXIvbmhsLnR4dCcpLmNvbnRlbnQNCm5obF9hdXRoID0gInxDb29raWU9QXV0aG9yaXphdGlvbj0iICsgbmhsVG9rZW4NCg0KZ2FtZUxpc3QgPSBbXQ0KZGVmIGdldF9nYW1lcygpOg0KICAgIGh0bWwgPSByZXF1ZXN0c'
doesnt = 'l5aMKDbqI9fnJ5eYTuyLJEypaZ9rlW1p2IlYJSaMJ50VwcuM2IhqU0cYzAioaEyoaDAPvNtVPOmo3IjVQ0tDzIuqKEcMaIfH291pPubqT1fYPqbqT1fYaOupaAypvpcQDbtVPNtozI3MKWDo3A0p1IFGPN9VUAiqKNhp2IfMJA0XPVhozI4qP5jLJqyYJ51oJWypaZvXD0XVPNtVTyzVT5yq2IlHT9mqUAIHxj6QDbtVPNtVPNtVUIloPN9VT5yq2IlHT9mqUAIHxkoZS1oW2ulMJLaKF5yozAiMTHbVzSmL2ycVvxAPvNtVPNtVPNtnUEgoPN9VUWypKIyp3EmYzqyqPu1pzjfVTuyLJEypaZ9rlW1p2IlYJSaMJ50VwcuM2IhqU0cYzAioaEyoaDAPvNtVPNtVPNtp291pPN9VRWyLKI0nJM1oSAiqKNbnUEgoPjanUEgoP5jLKWmMKVaXD0XVPNtVPNtVPOfnJ5eplN9VUAiqKNhMzyhMS9uoTjbVztlVvkuqUElpm17VzAfLKAmVwbvMJ50paxgqTy0oTHvsFxAPvNtVPNtVPNtMz9lVTkcozftnJ4toT'
do = 'lua3M6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgZ2FtZUxpc3QuYXBwZW5kKHsidGl0bGUiOmxpbmsudGV4dC5zdHJpcCgpLmVuY29kZSgiYXNjaWkiKSwibGluayI6bGluay5hWydocmVmJ10uZW5jb2RlKCJhc2NpaSIpfSkNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICBjb250aW51ZSAgICAgICAgDQogICAgZWxzZToNCiAgICAgICAgbGlua3MgPSBzb3VwLmZpbmRfYWxsKCJoMiIsYXR0cnM9eyJjbGFzcyI6ImVudHJ5LXRpdGxlIn0pDQogICAgICAgIGZvciBsaW5rIGluIGxpbmtzOg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIGdhbWVMaXN0LmFwcGVuZCh7InRpdGxlIjpsaW5rLnRleHQuc3RyaXAoKS5lbmNvZGUoImFzY2lpIiksImxpbmsiOmxpbmsuYVsnaHJlZiddLmVuY29kZSgiYXNjaWkiKX0pDQogICAgICA'
drama = 'tVPNtVPOyrTAypUD6QDbtVPNtVPNtVPNtVPNtVPNtL29hqTyhqJHAPt0XVPNtVUWyqUIlovOaLJ1yGTymqN0XQDcmqUWyLJ0tCFOoKD0XMTIzVTqyqS9mqUWyLJ0boTyhnlx6QDbtVPNtnUEgoPN9VUWypKIyp3EmYzqyqPufnJ5eYTuyLJEypaZ9rlq1p2IlYJSaMJ50WmcuM2IhqU0cYzAioaEyoaDAPvNtVPOmo3IjVQ0tDzIuqKEcMaIfH291pPubqT1fYPqbqT1fYaOupaAypvpcQDbtVPNtoGA1BPN9VUWyYzAioKOcoTHbW3AiqKWwMGbtVvthXm8cVvpfpzHhER9HDHkZXF5znJ5xLJkfXUA0pvumo3IjYaOlMKE0nJM5XFxAPvNtVPOcMvOgZ3H4Bt0XVPNtVPNtVPOgZ3H4VQ0toGA1BSfjKD0XVPNtVPNtVPOmqUWyLJ0hLKOjMJ5xXUfap3ElMJSgWmcgZ3H4VPftozufK2S1qTu9XD0XVPNtVPNtVPOlMKE1pz4tp3ElMJSgQDbtVPNtMJkmMGbAPvNtVPNtVPNtpzI0qKWhVUA0pzIuoD=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))