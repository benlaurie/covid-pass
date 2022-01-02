import base45
import cbor
import json
import sys
import zlib

from cose.messages import CoseMessage

def unpack_HC1(s):
    if s[:4] != 'HC1:':
        return None
    decoded = base45.b45decode(s[4:])
    decompressed = zlib.decompress(decoded)
    covpass = CoseMessage.decode(decompressed)
    return cbor.loads(covpass.payload)

print(json.dumps(unpack_HC1(sys.stdin.read()), indent=2))