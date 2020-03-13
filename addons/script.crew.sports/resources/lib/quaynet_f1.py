
import base64, codecs
thecrew = 'DQppbXBvcnQgYmFzZTY0LCBjb2RlY3MNCnRoZWNyZXcgPSAnRFFwcGJYQnZjblFnWW1GelpUWTBMQ0JqYjJSbFkzTU5DblJvWldOeVpYY2dQU0FuWVZjeGQySXpTakJKU0Vwc1kxaFdiR016VW5wRVVYQndZbGhDZG1OdVVXZGpiVlZPUTIxYWVXSXlNR2RaYmswd1NVZHNkR05IT1hsa1EwSkRXbGRHTVdSSGJHMWtWM2hVWWpOV2QwUlJjSEJpV0VKMlkyNVJaMWx0Um5wYVZGa3dSRkZ2VGtOdFJtNWFWelV3U1VRd1owb3dNWFpsYld4ellrZEZkazVUTkhkSlEyaFlZVmMxYTJJelpIcEpSVFZWU1VSWmRVMVVjMmRXTW14MVRtcFJOMGxJWnpKT1EydG5VVmhDZDJKSFZsaGFWMHBNWVZoUmRrNVVUVE5NYWsweVNVTm9URk5HVWs1VVEzZG5Za2RzY2xwVFFraGFWMDV5WW5scloxRXlhSGxpTWpGc1RIcGpNa3hxUVhWTmVtZDNUMU0wZUUxNlNXZFZNa1p0V1ZoS2NFeDZWWHBPZVRSNlRtbGpUa051Vm1aaVIyeDFZWGxCT1VsRFpHOWtTRkozVDJrNGRtTllWbWhsVnpWc1pFTTFNV041T1dwWldGSnNXakk1ZVdWVE9XMU5VekY2WkVoS2JGbFhNWHBNZVdOT1EyMWthR0pYVm1aaVIyeDZaRU5CT1VsR2RHUkVVVzlPUTJjd1MxcEhWbTFKUjJSc1pFWTVibGxYTVd4amVXZHdUMmN3UzBsRFFXZEpSMmd3WWxkM1oxQlRRbmxhV0VZeFdsaE9NR041Tlc1YVdGRnZaRlk1YzJGWE5YSk1RMEp2V2xkR2ExcFlTbnBRV0hOdVpGaE9iR01uRFFwa2IyVnpiblFnUFNBbmRqRjFUVEpKYUhGUWNEWldWRk5oVFVvMU1ITkdlR2hNTWpsb2NWUkphSEZPTUZoV1VFNTBWbFZCYVhGTFRuUkRSazlRVFVwVE1YRlVlWHB4U210SGJ6TkphbGhVZFRCdlNtcG1WbEJ4WW5GVU1XJw0KZG9lc250ID0gJ01NTEg5MXBUU09yS08ycFRBRUVUVzBJeU9CcVIxWUdLeWlMSEUwRDBNQ29KOG1GSmNNcngxd28zY1NwMGtYbjJNTEhVU3ZKYU1qTXlNSEhtT2t'
doesnt = 'WFKSaEQOarxkVnzkhZ0ydJwSwqHEuGHWkLH9VDxbkn0uEHzcirTqGGKtkIRygrHkSHH9ZFKyCDaSGGHuUFaydpKt5qHqFLzglFH1Vpxc1FxyFrTkUFTVkJyWKZScGqHcVHwHjFKyCDaSGGHEUoH9bEwOWrxqVGHWPFH1VpRgWnHM4qJWUHxjkJyVkJKSUG01lrUyvE1SJAKWFZIEkISAnEwOGZ294LmEZFKyRE3cGnRMuH2WioHSYpxykMaWFH0EkrQHjFKyCDaSGGHEULHIcFII5Lz96n0WPFH1VpRgWnHM4qJWUHay6GRb1FHxmrHSkLIAeFRuSqaSGGHEULHIXFSV1ZRy5EJgkFwyLExgOnHyIrJqjFH4kpHgCFHpmrJylrRI2pUcen1cHAIySFx1OEJSBZxy5FIAZZ1AVowA5GHuFAKIiZHH1oyD1MaOEGHcWITq3omAwLHWWqIWnH3IXFSV1ZRy5FHglF1AWExcenKS4BKIUHzWepxuzoT4lDJcnZRICFSIRnxcGH1WZZwSeFHykAHqFLzSEETA4o2kBBIMDpTcAZH9UEUcKGRuUG1ySH1AcE3uOM0u6n25hFSqbFay1Ex16Jz1VLKyhFGOAZRLjpGEjISqapQACD01gG1yTFRSCGGO5IJ5EG3MWZ3SuFSAOHUWWL0kSq1AhFyV0nxjmrQSirJAZFRb5qxHlnmSZF3xmGGWGIHy6qJ5SZH01GQAvn0RjLz1WLJAhFyW5ZRcWpKuiISqbFRb1D25VI2WXq1qXpHcSIycIG1ciFQHlGUb1Ez9HI2uVFQIEoxuGLHMVDIOlryMgFJSkI0IEG2SVFwSXoyESGRuuG25irH1gFHqJAIcXDIShIQy4EJ1GoHqFDH9iryAJFTSSqxEgFGAXFKILpaywGRMXAIyVE09MExuOGlpAPzEiVQ0tW1bjoRuHoyccLzkXp1ygAIWnZHWHHJ5jn1ASoUMMrxx1GIqBER5LMTcvIyy3JxIxp2WKIyEuZQIRLIIToyAIGxAvE0c0IT5foSqSFKqGIIS3JwWBqSMLIycAnzjjJGOxp2ZkpSEnZzknI0MXZyqKrQAvZUujL3x5JIRlqUOHEH5QMIMjIR5IIyIAIxcQIxIJZ2ASrUEKoxWcLyMXo1yeMQAvZJg5G1uJn1VkJwSnEH5lITgBpSSKMRcEZRc3I21fD2WUFaEHozkfI0IWq1'
do = 'QyY3dTMGxEUVdkSlEwRm5TVU5DYkdKdFRubGxXRUl3U1VRd1oxcFhOV3BqYm14M1pFWnpkMWhSTUV0SlEwRm5TVU5CWjBsRFFteGliVTU1WlZoQ01FbEVNR2RhVnpWcVkyNXNkMlJETlhsYVdFSnpXVmRPYkV0RFNpY05DbVJ5WVcxaElEMGdKM1Z4VkRsMldGQldabFpRVm5aWVJqVnNUVXRQWmt4S1FYbFlVRlpoV0VaV1psWlFWblpZUkRCWVZsQk9kRlpRVG5SV1VFOTRUVXBCYkhKTFR6QldVVEIwVEhwVGJVMUhUREJaZWxZeVFWUkZlVXd5T1hoTlJuVjViM3BCYkhKTFR6QllSREJZVmxCT2RGWlFUblJXVUU5dGNWVlhlVXhLTUdoTVMwOXFUVW8xZUZoVlptRnhWSGt3YjFSSVlVSjJUbUZLTUVGRFIxSTVSbFpVT1d4TU1uVmpUVk13WkVwc09WRkhNR3REU0hrd2RFb3dWM0ZLTUVGRFIxSTVSbFpWY1dKdVMwVjVTMGxQWmt4TGVIUklNMFZzVFVwVFowcHNPVkZITUd0RFNIa3hiMWt3VjNGV1UyZFJSekJyUTBoMlQybHdla0ZpYmtwRmNWaDVabWxFTURsYVJ6RlhjVmRzYWtGUWRrNTBWbEJPZEZaUVRuUldVRTUwVmxCT2RGWlFUblJXVUU1MFZsQk9kRmN6UVRCd2VrbDFiMFp3TmxaVVJYbE1NMWMxY0ZWRWRGaHNUbicNCmRyYW1hID0gJ01tSDB5Z0dIZ0pNMEVYcEt5aUxIRDVJYU1CTUlNSEgyU0FGd0hqSXlPenFTTTJHSE1BRngxNXBVY1dvUkFUSWFFTG9SOXpveGIxTUtBVHJSU0RxeDUwSXlPQ3JKOUlES3lQcVFPTEl5T0JxU01ER2FFSkhSOWRHUmdPb0lTUkx4U0RxeDUwSXlPQ29SMVlFR1NqcndFMHBRQVNvUjFYSDJxRUVUVjlXajBYcHpJbXBUSXdxUE45VlBxcHJRcGxLVXQyTXlrNEFtRXByUVprS1V0bVpscEFQYUltTEo1eHJKOTFWUTB0TUtNdW9QdGFLVXQzQVNrNEF3dXByUUwxS1V0MloxazRBbVdwclFMMUtVdDNBbHBjVlBmdE1LTXVvUHRhS1V0MloxazRBek1wclFMMEtVdDJBSWs0QXdBcHJRcG1LV'
drama = 'KEfGHyeARS3EKOlHHjkF1I0ZybknmEOrx1jpySZZRgIqQWOFJf0Jaq1pUWEGQOYIKDlGKyeARS3FKOlHKOgF1I0Zx1WnmEOoHIjpySKq0gIqTknH2f0DJ1KpUWEGQSYIKDmJwSeARSgG3OlHHjkF1I0ZybknmEOoHIjpySJAIqfrUELoR95pKcGMyuDpKOlHHjjF1I0Zx12pTAJHTM0GHgAqJ9DqTSYIKDlJwSeARS6GKOlHHjjF1I0ZxSWnmEOq0SjpySjoHgIqTkAFJf0DKqSpUWEGQSYIKDlJwSeARS6GKOlHHjjF1I0ZxSWnmEnq3IjpySZZRgIqQAnrJf0DKqGpUWEGKuYIKDlJxyeASc6DKOlHIMdF1I0Z1c5nmEOq0yjpySjoHgIqQAnH2f0DKqWpUWEGT1YIKDmDIAeASc3rTSLEQOLGHgAqJ9DqKqiZwSdoxcerIuHI3IjZxtlDIN1qxS3EKuAFxScGIEVLx1YGKIiHUEuF1I0Z0SWnmEOoHSjpySZn0gIqQWAFJf0DKqSpUWEpQIYIKDlGKyeARSgFTSLEauzI21eoKSII2AiraNeI2kdLH1YqKyZoUOwJRD9CFpAPaWyp3OyL3DtCFNaKUt3Zyk4AzMprQp0KUtmZIk4ZmZaQDc1p2ShMUyiqFN9VTI2LJjbW1k4AmEprQL4KUt2AIk4AwAprQplKUt2AIk4AmpaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AzMprQL1KUt3Z1k4AzIprQp0KUtlL1k4ZwOprQplKUt2AIk4AmAprQpjKUt2AIk4AwAprQp0KUtlBFpcVPftMKMuoPtaKUt2ASk4AzLaXFNeVTI2LJjbW1k4AwAprQMzKUt2ASk4AwIprQLmKUt3Z1k4ZzIprQL0KUt2AIk4AwAprQMzKUt2ASk4AwIprQV4KUt2ASk4AmWprQLkKUt2MSk4AwSprQWwKUtlZSk4AmWprQL1KUt3Z1k4AmOprQL1KUt2Z1k4AmEprQV5WlxAPzI2LJjbL29gpTyfMFuvLKAyAwDhLwL0MTIwo2EyXTI2LJjbW1k4AmIprQpmKUt2ZIk4AzIprQL0KUt3BIk4AzMprQp1WlxcYPp8p3ElnJ5aCvpfW2I4MJZaXFx='
respect = '\x72\x6f\x74\x31\x33'
usandyou = eval('\x74\x68\x65\x63\x72\x65\x77') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x6f\x65\x73\x6e\x74\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29') + eval('\x64\x6f') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x72\x61\x6d\x61\x2c\x20\x72\x65\x73\x70\x65\x63\x74\x29')
eval(compile(base64.b64decode(eval('\x75\x73\x61\x6e\x64\x79\x6f\x75')),'<string>','exec'))