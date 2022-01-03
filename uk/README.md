# UK COVID Passes

These come in two flavours, domestic and international.

The international pass is a standard [EU Digital COVID Certificate](../eu).

The domestic pass is based on the [EU Digital COVID Certificate](../eu) but does not conform to the standard. Since NHS Digital have declined to document it, I'll do it for them.

## Domestic Pass Format

As mentioned above, this is a standard EU pass, but instead of the content being one of `v`, `t` or `r`, instead it uses `d`. Also it claims to be version 1.0.0 rather than the current (at the time of writing) 1.3.0.

Something like this:
```
{
  "1": "GB",
  "4": 1638798448,
  "6": 1641476820,
  "-260": {
    "1": {
      "d": [
        {
          "ci": "URN:UVCI:01:GB:XXXXXXXXXXXXXXXXXXXXXXX",
          "co": "GB-ENG",
          "df": "2021-12-06T13:47:28+00:00",
          "du": "2022-01-05T13:47:00+00:00",
          "is": "NHS Digital",
          "pm": 120,
          "po": [
            "GB-ENG:1",
            "GB-ENG:2"
          ]
        }
      ],
      "dob": "1970-01-01",
      "nam": {
        "fn": "Bloggs",
        "gn": "Joseph Archibald",
        "fnt": "BLOGGS",
        "gnt": "JOSEPH<ARCHIBALD"
      },
      "ver": "1.0.0"
    }
  }
}
```

The contents of the `d` section are:

| key | value |
| --- | ----- |
| `ci` | The unique ID |
| `co` | The issuing country (an ISO 3166 subdivision) |
| `df` | The start date |
| `du` | The end date |
| `is` | The issuer |
| `pm` | *UNKNOWN* (let me know if you know!) |
| `po` | A list of vaccinations in the format `GB-ENG:n` where `n` is the sequence number of the vaccination |

## Historic UK Domestic Pass Format

Prior to somewhere around October 2021, the UK Domestic pass consisted of three base 64 encoded strings, separated by `.`s. The first is the key ID, the second is version + expiry (yyMMddHHmm) + name (where '+' is concatenation) and the third is a signature.

## Some Observations

- Although the `ci` field is supposed to be unique per vaccination (at least in EU passes), the UK uses the same ID for all vaccines for the same person in international passes.
- I have seen UK Domestic passes where the wrapper dates are reversed - meaning they can never be valid.
  - However, the NHS COVID Pass Verifier still verifies them.
- Sometimes the numeric keys appear as numbers, sometimes as strings.
- For no obvious reason boosters (or third vaccinations) seem to appear in their own domestic certificate, unlike doses 1 and 2 which appear in the same certificate.