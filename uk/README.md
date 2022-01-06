# UK COVID Passes

These come in two flavours, domestic and international.

The international pass is a standard [EU Digital COVID Certificate](../eu).

The domestic pass is based on the [EU Digital COVID Certificate](../eu) but does not conform to the standard. Since NHS Digital have declined to document it, I'll do it for them.

Note: since I started this document, NHSX have informally provided some definitive information about the contents of the domestic pass, which I include below. Hopefully they will soon release proper documentation.

## Domestic Pass Format

This format is used by England, Wales and Scotland (see below for the Scottish variant). It is currently unknown what format Northern Ireland uses.

As mentioned above, this is a standard EU pass, but instead of the content being one of `v`, `t` or `r`, instead it uses `d`. Also it claims to be version 1.0.0 rather than the current (at the time of writing) 1.3.0. NHSX say this is to avoid confusion with the EU passes (an odd choice in my opinion). In future they will change the encoding to start with `UK1` instead of `HC1` (a far better choice, in my opinion).

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
| `pm` | "Policy mask" - a (more) detailed list of criteria met (let me know if you know more! Values seen so far: `120`, `123`, `8`)[1] |
| `po` | A list of polices the subject met the criteria for at the time of vaccinations (see below) |

[1] NHSX say this field is unused (presumably by verifiers, since it most certainly is used in passes) and will be phased out.

## Policies

| id | meaning |
| -- | ------- |
| `GB-ENG:1` | *UNKNOWN* |
| `GB-ENG:2` | *UNKNOWN* |
| `GB-ENG:3` | [England's domestic pass policy on 5 January 2022](https://web.archive.org/web/20220105223257/https://www.nhs.uk/conditions/coronavirus-covid-19/get-digital-covid-pass/)[2] |
| `GB-SCT:1` | [Scotland's domestic pass policy on 6 January 2022](https://web.archive.org/web/20220106104516/https://www.gov.scot/publications/coronavirus-covid-19-certification-scheme-information-for-customers/pages/prove-vaccine-status/)[2] |

[2] The most recent date available at the time of writing.

## Scottish Domestic Pass

The Scottish pass follows the same format, but
- The `co`, `dob` and `nam` fields are not filled in.
- `df` and `du` do not include time.
- The validity period is (currently) 3 days instead of a month.

## Historic UK Domestic Pass Format

Prior to somewhere around October 2021, the UK Domestic pass consisted of three base 64 encoded strings, separated by `.`s. The first is the key ID, the second is version? ('1') + expiry (yyMMddHHmm) + name (where '+' is concatenation) and the third is a signature.

The meaning was "meets with current COVID pass criteria".

## Some Observations

- Although the `ci` field is supposed to be unique per vaccination (at least in EU passes), the UK generates a new one per certificate issued and uses it for all passes in that certificate.
- I have seen UK Domestic passes where the wrapper dates are reversed - meaning they can never be valid (NHS Digital claim this is now fixed).
  - However, the NHS COVID Pass Verifier still verifies them.
- Sometimes the numeric keys appear as numbers, sometimes as strings.