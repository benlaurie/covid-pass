EU Digital COVID Certificates are documented in various places:

- [JSON Schema](https://github.com/ehn-dcc-development/ehn-dcc-schema).
- Technical Specifications for Digital Green Certificates [Volume 1](https://ec.europa.eu/health/sites/default/files/ehealth/docs/digital-green-certificates_v1_en.pdf), [Volume 2](https://ec.europa.eu/health/sites/default/files/ehealth/docs/digital-green-certificates_v2_en.pdf) and [Volume 3](https://ec.europa.eu/health/sites/default/files/ehealth/docs/digital-green-certificates_v3_en.pdf).
- [Technical Specifications for EU Digital COVID Certificates JSON Schema Specification](https://ec.europa.eu/health/sites/default/files/ehealth/docs/covid-certificate_json_specification_en.pdf) - this contains a detailed explanation of the contents in the most readable form I've found so far.

The function `unpack_HC1` in [unpack_hc1.py](unpack_hc1.py) will take the content of a pass (usually from a decoded QR code) and return the contained JSON.