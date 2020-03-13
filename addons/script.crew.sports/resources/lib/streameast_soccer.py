
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnRFFwcGJYQnZjblFnWW1GelpUWTBMQ0JqYjJSbFkzTU5DblJvWldOeVpYY2dQU0FuWVZjeGQySXpTakJKU0Vwc1kxaFdiR016VW5wRVVYQndZbGhDZG1OdVVXZGpiVlZPUTIxYWVXSXlNR2RaYmswd1NVZHNkR05IT1hsa1EwSkRXbGRHTVdSSGJHMWtWM2hVWWpOV2QwUlJjRzFqYlRsMFNVaEtiR015T1RGamJVNXNZM2sxYzJGWFNXZGhWekYzWWpOS01FbEhUbTFqTWs1NVdWaENiRVJSYjA1RGJVWnVXbGMxTUVsRU1HZEtNREYyWlcxc2MySkhSWFpPVXpSM1NVTm9XR0ZYTld0aU0yUjZTVVUxVlVsRVdYVk5WSE5uVmpKc2RVNXFVVGRKU0djeVRrTnJaMUZZUW5kaVIxWllXbGRLVEdGWVVYWk9WRTB6VEdwTk1rbERhRXhUUmxKT1ZFTjNaMkpIYkhKYVUwSklXbGRPY21KNWEyZFJNbWg1WWpJeGJFeDZZekpNYWtGMVRYcG5kMDlUTkhoTmVrbG5WVEpHYlZsWVNuQk1lbFY2VG5rMGVrNXBZMDVEYmxabVlrZHNkV0Y1UVRsSlEyUnZaRWhTZDA5cE9IWmtNMlF6VEc1T01HTnRWbWhpVjFab1l6TlJkV0pIYkRKYVV6bDZaRWhLYkZsWE1YcE1NMDUyV1RKT2JHTnBPRzVFVVhCdVdWY3hiRmd5ZUhCak0xRm5VRk5DWWxoUk1FdEVVVzlPUTIxU2JGcHBRbTVhV0ZKbVdqSkdkRnBZVFc5TFZHOU9RMmxCWjBsRFFucFpNMHBvWTBkV2VVbEVNR2RaTWxwNldUTkthR05IVlhWWk0wcHNXVmhTYkZnelRtcGpiVVozV2xoSmIwdFJNRXRKUTBGblNVZG9NR0pYZDJkUVUwSjZXVE5LYUdOSFZubE1iV1JzWkVOb01WZ3llSEJpYlhOelNVZG9iRmxYVW14amJrMDVaWGxrTVdNeVZubE1WMFp1V2xjMU1FcDZiMmRaVjJSc1ltNVNPVXRUTldwaU1qVXdXbGMxTUVSUmIyZEpRMEZuWXpJNU1XTkRRVGxKUlVwc1dWaFdNR0ZYV2pGaVJrNTJaRmhCYjJGSVVuUmlRM2RuU2pKb01HSlhkM1ZqUjBaNVl6SldlVXA1YTA1RGFVRm5TVU5DYUVsRU1HZGpNamt4WTBNMWJXRlhOV3RZTWtaellrTm5Ua05wUVdkSlEwRm5TVU5CWjBveVVuQmthV056U1VkT2MxbFlUbnBZZWpFM1NqSk9kbUpETVhSYVF6QjZTVWRPZG1KRE1UUmplVEF6U1VoQ2FGcEhVbkJpYldOMFltNVdjMkpEUWpCYVdHZ3dURmQ0YkZwdVVXNW1VMnRPUTJsQlowa25EUXBrYjJWemJuUWdQU0FuVUU5NmJ6TldkRTFVVXpCTVJrOWpiM1pQZFVKME1GaFdVRTUwVmxCT2RGWlFUekJ1UzBWbVRVWk9PVlpVUlhWeFZGSm9UWHA1YUUxUWRHRk5WSGt5VjJ4cWRFd3lhM1Z3TTBGelEwdG1ZWEZVU1gnDQpkb2VzbnQgPSAnSWlFYVI1SlJMMVpSMVlxR09FRVRXMEl5T0JxU01ER2FFSklVUzFvMGNXcDI5SHJKMWtIUUkxcFNJQ3JKOTZFVFdsb1VSam94Z1NNeDFUcFFNSk'
doesnt = 'yVFKqjFHIypxy5AxMXqIcnq3x0E0uAZREWGmWULHIXFSV1ZRy5G0WkH01RE2SSFxuIHmSjHIqCGQV1IUOHGHcVIIA3E0qJZJ5YGmMTISAZEKqWARqVL09hFQSVEyEKF1bjrTcUF0kdDIAkMz5uEHgnLKy1omAvAJ9FZIEjIRSgEJS1G0uIETcXH01RE2SSFxyWpGIjFHyKo1D5ZxplH1cTq1Z1Ez1KMHjmGz1SHyARpISCGRy6n0AhLH82pxc1n0uIFKIUFTqGpQNjoRtlpHSTZJA2FyWAAREWGmOnH3ISEIEOM3OWFHglFTgLJyISHHI4BJyTZREdFyAGHxk4H0ElrRx1E0gAD0kVZIySF0SdJwOWMxqVL0qAZKIVpRgWnHM4qKqRLHEdFyAAERquEHcWFSZmpSIwE254ZIyWLHIEEKt5Z0qXH09kZ082FQWwDHI3FGAjIJAKpHgGFRMYDJcnrSAzE1WaD3WYGmWkIRSSEIEKZRy5G0WkIQIWEHcknHuFAQIWrHyCpGACAxtlL0STZH1vE0qKI1cGqHyTF0ScFII5Lz96n2EkIQIVExgWDHyFrJMjIQOeDGSjoHMXZHSTZH1uE1Wwn3WXBKISISADpKt5ZHqUI1qhIIAWJyEOGKW4H2AiZyAGpxb5qHIFH0EkrQHjFKyCD29XBT1TFzAXFRqCZRIIL1qkF1AMEHcODHkVrKcTHIL1JxgCEUSXI2gWHIA6FxyCDxkXAHySFaScFSSWMRqFM0giFQSMFKcGGRIEG0kWrH9PpIAAFRuuEISSrQyao21OI255rGMUFxScpauWoHqFL2IArKIPJyA1FxuFAGOWrH9PpIAAERq6H0SWIKufFGWeMUSFnzkhZ0ydJwOGoHDjM3cZFTcfDxcAGHM3HmEXFUShpIWdoRWXGH1TZ0yaFxuknaSIG0uVZ3IOFII5LxqXnzghIIALowWAFxyVFGIjrHyFGGV5FRMYL2gVIIV1FyWRnxcGGHEULHIXFIVkL3OIGHAlHzgMEHgWFxyIrJWWrHITDKyGHxkuEHcVHwHjFKyCDaSGGHySFxSeFIEaAHy5HzckHwSVFT1CJxI3FGMirTWuHHEwrT9fGwyJHUNkowOaHH1HM3IXH3ybE1WOHT56I1ISLJA3Jxq0AH1YrKunH2AYEJSSJScgG2cUIQITo1EWIxuVAIShFSAuExuOG00jrISRFaS1EyWwMxc6rH9PFUyIFUc1rRHjFGSXFH1go3cGIxM6n25hFxI4EIAGnH0jrISRFaSKEQOGLHMVDHSAZxSJEzSCqz95H2yAHaSzJyEKIHyYDKITHzAzFac5MHq4DJARFaSKEQOGLHMVDH9AZUugoyE5qxxjAJuAH3SypHyKIJ9HqKMSoKybEwOOMKSXEIIWq0I4EyAwnxc5qKuiIRSwGGV1ExcFLmIZq0SKo3ueHHEuL3uTHaycFaukIScGrHqhZ09FFRb5LHMVDH8aQDcxolN9VPqnZTkRHIqxFyVlrUEGIJEeLHqXJSMKMTuJryWhJxIxp01UFxuJIScSIIp5oyAIGxWnZTkRHIqxFyRjEz5GIH5QGIqBqTDlMSSIZRc2JGVkI2WIHyWvZzEXHGOToyAIGxWnZTkRHIqxFyRjFaMnEJA4LmOfEH1UMTcAnmH1I1MbD2WUGaOBImIuI0MTqycTnRgwZUuRHJ05LILjJaWKoTuYMJkPJJZlAJgKEGImJGWerTSTo3yJoyMeHGWAZyAIMRqvoUOLGyEPoIHlqQSK'
do = 'VEk1ZFdSSFZuVmtRVEJMU1VOQlowbERRV2RKUTBGblNVTkJaMk15T1RGalEwRTVTVVZLYkZsWVZqQmhWMW94WWtaT2RtUllRVzloU0ZKMFlrTjNaMG95YURCaVYzZDFZMGRHZVdNeVZubEtlV3RPUTJsQlowbERRV2RKUTBGblNVTkJaMGxIV25sWlZ6RnNTVVF3WjJNeU9URmpRelZ0WVZjMWEwdERaSEJhYmtwb1lsZFZia3RSTUV0SlEwRm5TVU5CWjBsRFFXZEpRMEZuWVZkWloxcHVTbWhpVjFVMlJGRnZaMGxEUVdkSlEwRm5TVU5CWjBsRFFXZEpRMEZuV201S2FHSlhWV2RRVTBKdFkyMUdkRnBXYzI1ak0wcHFTakV3VGtOcFFXZEpRMEZuU1VOQlowbERRV2RKUTBGblNVTkNkRmxZVGpCYVdFbG5VRk5DZWxrelNtaGpSMVo1VEcxa2JHUkRhRzFqYlVaMFdsTjNaMkZIVm1oYVIxWjVZM294TjBvelNteGFiVlo1V2xoSmJrOXBRakZqYlhnNVMxTTFhbUl5TlRCYVZ6VXdSRkZ2WjBsRFFXZEpRMEZuU1VOQlowbERRV2RKUTBGbll6STVNV05EUVRsSlJVcHNXVmhXTUdGWFdqRmlSazUyWkZoQmIySlhSbnBrUjFaNVRFTkJibUZJVW5SaVF6VjNXVmhLZWxwWVNTY05DbVJ5WVcxaElEMGdKMkZZUkRCWVZsQk9kRlpRVG5SV1VFNTBWbEJPZEZaUVRuUldWREJ0Y1VkMGRFTkdUMnhOUmpWM2J6SXhhbTVLYTNsWVVIRnRiek5KYkV3eVNEWldVRlppV1habUwxaEdWbUZaVGpCWVZsQk9kRlpRVG5SV1VFNTBWbEJPZEZaUVRuUldVRTUwVmxCT2RGWlFUblJXVUU1MFZsQk9kRlpRVG5SV1ZWZDVXWGhGUTBsU1UxcEhVSGhvVFhwNWFFMVVVMlp2VUhWdGNWVldZbkF5T1RGd1VEVnFjSHBKTUhGVWVYcHlSbmhqVVVSaWRGWlFUblJXVUU1MFZsQk9kRlpRVG5SV1VFNTBiMGRCTVVKUVRqbFdWREJ0Y1VkMWIxcFRNRUZRZGs1MFZsQk9kRlpRVG5SV1VFNTBWbEJPZEZaUVQyZGFNMGcwVmxFd2RHOUhRVEZDVUU1bFZsQnhPRWxMUVhsd2RqRlBUVEpKYUhGUk1HRldVR1owVEVweGVXOWhSSFJZYkU1aFYzbFhlVTE2U1d4TlMxWTVWMnhPWlZaVVRXeE1TakY1VVVSaWRGWlFUbicNCmRyYW1hID0gJ0VKSFI1MEl5T0JxU01ER2FFSkhSNTBwUUFTb1IxWEgycU1yeUFkcFNFV25SMURxUlNEcXg1MEl5T0JxU01ER2FFSkhSNTBJeU9CcVNNREdhRUpIUjUwcHpra1pUNVlFSk1BRWFOMkl5T2tvMERqQkljVVpJTTBvbUFLcTI1SHJLdVlFekFpSkdPT0QwcUZCSE1ZRXg5aUVVeGtvMERqQkljVVpJTTBwR1cxTDNTSEZLU1ZJVGcxcHhNQ0UzU0lJM3laRndTaUpHT09EMHFGQkhNWUZKTWNFVXhqcVJiakRIQVVId3lUSXlENW9SamxxSkFBSG1PeEZ6ajVISHBqbjBBVnJHT3VKSU9CTEtObUVKa0FGeUFhSTIxdnFUOVVER1NQSUdPd0hIRXZxU01ER2FFSkhSNTBJeU9CcVNNREdhRUpIUj'
drama = 'HjE1EGF3WVn1uArSARpKt1ZRy5G0WkH01RE2SSFxuFAGOWrHIKGJSBoRMEGHISISpjFKyCDaSGGHEULHIXFSV1ZRy5G0WkH01RE2SSJxkWpGIUHzA6ERyCZxquEHcVHwHjFKyCDaSFZIuhZwSOEGWKG0uIGHWkH01RE2SSFxuFAGOWrH9PpIAAFREXrJyZFRy3omWGI3WWH1WZrSARpKt1ZRy5G0AiHwSMEHqGnaW3EGOjHHSGo1VkJRtlpHISISqCFSIRnxcGGJMUZzAdpzS5LaOWGmSZFQSMEHgOnybjFJMUFTAUGGS1EUOWEIETHHyQEGSKMHqWpJMlIRSSEIEJBIqdZSujrxygpSEWq3SDGwyJHUSjpySjoRgIqQWArJf0DJ1SpUWEJzgYIKEgJzkjDIOuFJ1ZFwI4pxb5ZIMEZUEAF011o1O0LHgIqQAOH2f0DKq1pUWEGQSYIKDlJwSeARSgI3OlHHjkF1I0Z0SfpTAJHTM0GHgAqJ9DqTSYIKDlJwSeARS6GKOlHHjjF1I0ZxSWnmEOq0SjpySjoHgIqTkAFJf0DKqSpUWEGQSYIKDlJwSeARS6GKOlHHjjF1I0ZxSWnmEnq3IjpySZZRgIqQWArJf0DKqWpUWEpT1YIKDlGHyeARSgEKOlHIq3F1I0oScGnmEOoIqjpySZZHgIqQAnZJf0DJ1CpUWEGQSYIKDlJwSeARSgEKOlHIL1I2k4qSufG3ykryAzJSOkpUWEGQOYIKDlGKMjL1MDMaEAF011o1O0LHgIqQWnZJf0DKcApUWEGQOYIKDlDHyeARS3DKOlHKOgF1I0oR1WnmEOq0IjpySZZHgIqQWnZJf0DKcApUWEGQOYIKDlDHyeASc3qKOlHHjjF1I0Z1c5nmEOq1AjpySArRgIqQWnFJf0JacOpUWEIzcYIKDmJayeARS3FKOlHKOgF1I0Z1cGnmEOq0yjpySZoHgIqQAOH2f0Jaq4LIuRZSuAF011o1O1q28lZJchFzg5JSEKqKNlFQWOHQI2DKqSrR1XDJyAIRuvGHgAqJ9DqTSYIKDmDHyeARSgDKOlHHkeF1I0Zx1WnmEOq0IjpySjAHgIqQWArJf0DJ1VLIuTrTMKoJggpIIKL296pPgKoTcuGHg1rHkfpTALEQ09Wj0XpzImpTIwqPN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaImLJ5xrJ91VQ0tMKMuoPtaKUt3ASk4AwuprQL1KUt2Z1k4AmWprQL1KUt3AlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2Myk4AwIprQpmKUt2MIk4AmEprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxtXlOyqzSfXPqprQL0KUt2MvpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt3Zyk4AwSprQMxKUt2ZIk4ZzAprQVjKUt3Zyk4AwIprQpmKUt3ZSk4AwIprQLmKUt3ASk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3AIk4AmAprQLkKUt2MIk4AwEprQp5KUt2Myk4AmHaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))