
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnYVcxd2IzSjBJSEpsY1hWbGMzUnpEUXBwYlhCdmNuUWdjbVVOQ21aeWIyMGdZbk0wSUdsdGNHOXlkQ0JDWldGMWRHbG1kV3hUYjNWd0RRcHBiWEJ2Y25RZ1ltRnpaVFkwRFFvTkNtRm5aVzUwSUQwZ0owMXZlbWxzYkdFdk5TNHdJQ2hYYVc1a2IzZHpJRTVVSURZdU1Uc2dWMmx1TmpRN0lIZzJOQ2tnUVhCd2JHVlhaV0pMYVhRdk5UTTNMak0ySUNoTFNGUk5UQ3dnYkdsclpTQkhaV05yYnlrZ1EyaHliMjFsTHpjMkxqQXVNemd3T1M0eE16SWdVMkZtWVhKcEx6VXpOeTR6TmljTkNuVmZiR2x1YXlBOUlDZG9kSFJ3T2k4dmNYVmhlVzVsZEM1MWN5OWpZWFJsWjI5eWVTOXVZMkZoWmkxemRISmxZVzF6THljTkNtZGhiV1ZmYkdsemRDQTlJRnRkRFFvTkNnMEtaR1ZtSUdkbGRGOW5ZVzFsY3lncE9nMEtJQ0FnSUdoMGJXd2dQU0J5WlhGMVpYTjBjeTVuWlhRb2RWOXNhVzVyTENCb1pXRmtaWEp6Jw0KZG9lc250ID0gJ0NLZmFxS0F5cHYxdU0ySWhxUHA2VlRTYU1KNTBzRnhoTDI5aHFUSWhxTjBYVlBOdFZVQWlxS050Q0ZPUE1KUzFxVHl6cUprR28zSWpYVHUwb0p'
doesnt = 'dMyMDpJWkIQSzJJSCqKOuDKyjqaOwHHEvqSMDGaEAF015o2SRqRATG21iZ0ydJKcAL296EKAZFzgzJSOkLyc2pTMZF0HjpTSnBKWfpKqiISAgpTkjAyMuG2yjZ0EapIE5ZT9HFUMmEauOHUMBqSMDG3ciZ1M0GGWGM01TG2Aiqx95pKcWnUSELxSDqx50IyOBqSMDGaEkIUxjo1EVqRATG2SZFwS5JKcFnUSHFGEkHQI5o3cOnH1HFTWKZyAgGQW5L1qfnzShFaSbomAKrIqfrRSDqx50IyOBqSMDGaEiIUybozkBBIMHpKIiFxubGRyzLJ5II3yAqaSkHHEvqSMDGaEJHR50IyEkqJ9XFKAiIUygpIN1qKOIG3yirxEvpzkkZT5YEJMAEaN2pIE5ZT9HFTMKZzgwo3czLHW6n2Airzp5JRDjJSMDGaEJIIq5pIIWoT92G2SZFwS5FmWeL3NmERSDqQOLpQASoPpAPzEiVQ0tW1cKEaEWEQOaImRjGxAgHzknnHWhJyuFMzZmHaynI0M0F0q4pTWgp3OCMmOYFHAOM0yUnQOvI3qaHSAPrIcLEwSnJR4jL3x1oycLHJ9vE2k1LKy4o1cKEzgnJRc6HSumozELGzkwnGSbJwWJqJEQLmMMI2EfLz5FBHgGAJcvZwHjJyp1ZREEo2qWD0SaLmV5ZJAQDGyWEHcfJIuJZTSKJwSvEx52MSuOo2SVHaEvD3qhLHuFqTWQAKqMJRc6JyuWoxgEZRgWD0SaFHqBqz'
do = 'JuUmxiblFnUFNCemRISW9jMjkxY0M1d2NtVjBkR2xtZVNrTkNpQWdJQ0JsYm1OeWVYQjBJRDBnY21VdVkyOXRjR2xzWlNnaVlYUnZZbHdvTGlzL1hDa2lMSEpsTGtSUFZFRk1UQ2t1Wm1sdVpHRnNiQ2hqYjI1MFpXNTBLUTBLSUNBZ0lHbG1JR1Z1WTNKNWNIUTZEUW9nSUNBZ0lDQWdJR1Z1WTNKNWNIUWdQU0JsYm1OeWVYQjBXekJkRFFvZ0lDQWdJQ0FnSUdWdVkzSjVjSFFnUFNCbGJtTnllWEIwTG5KbGNHeGhZMlVvSW1GMCcNCmRyYW1hID0gJ28yVmJWdmp2VnZ4aHB6SWpvVFN3TUZ0dldseHZZUFZ2WEQwWFZQTnRWUE50VlBPeE1KQWxyS08wVlEwdEx6U21NR0wwWXpWMkFURXlMMjl4TUZ1eW96QWxyS08wWEQwWFZQTnRWUE50VlBPbXFVV3lMSjBoTEtPak1KNXhYVWZhcVR5MG9USGFCdk5hSjBBQ0dSOUZWVDlsTDJ1Y01TMGRKbDlRRzBrQ0h5MHRKMFdxSjBBQ0dSOUZWVXFibktFeUtJT2ZMS3h0SDNFbE1KU2dKbDlRRzBrQ0h5MW9ZMFdxVlNnUUcwa0NIdk9pcHpBYm5KRXFYeWZpRDA5WkcxV3FXbGpBUHZOdFZQTnRWUE50VlBOdFZQTnRWUE50VlBOdFZQTnRXM0EwcHpJdW9GcDZWVEV5TDNXNXBVRHRYbE52c1NJb'
drama = 'H1YIzqRFaS5o2SRBIM2GzIJISAuGHb1ZSMDMaEJqx1TGHcArKO6FJkQEyM0JTkCMz5XAJImEauOHUMBqSMDG3yiIHS5DaDjJSMDGaEJHR50IyOCnxkYDJ1EETWOHUMBqSMDG2kAF0HkpUb0qUNmEJkAFyAaHHEvCFpAPaWyp3OyL3DtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc1p2ShMUyiqFN9VTI2LJjbW1k4AmEprQL4KUt2AIk4AwAprQplKUt2AIk4AmpaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AzMprQL1KUt3Z1k4AzIprQp0KUtlL1k4ZwOprQplKUt2AIk4AmAprQpjKUt2AIk4AwAprQp0KUtlBFpcVPftMKMuoPtaKUt2ASk4AzLaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AmWprQLkKUt2MSk4AwSprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmIprQpmKUt2ZIk4AzIprQL0KUt3BIk4AzMprQp1WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFx='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))