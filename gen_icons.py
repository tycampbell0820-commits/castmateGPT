import base64, struct, zlib

def make_png(size, bg, fg):
    """Minimal PNG generator"""
    w = h = size
    # Create RGBA pixels
    pixels = []
    cx, cy, r = w//2, h//2, int(w*0.42)
    for y in range(h):
        row = []
        for x in range(w):
            dx, dy = x-cx, y-cy
            dist = (dx*dx + dy*dy)**0.5
            if dist <= r:
                # inner circle: fishing emoji style - dark green bg
                row.extend(bg)
            else:
                row.extend([0,0,0,0])  # transparent
        pixels.append(bytes(row))

    def chunk(name, data):
        c = zlib.crc32(name + data) & 0xffffffff
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', c)

    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))

    raw = b''
    for row in pixels:
        raw += b'\x00' + row
    idat = chunk(b'IDAT', zlib.compress(raw, 9))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

for size in [192, 512]:
    data = make_png(size, [14, 26, 20, 255], [125, 211, 168, 255])
    with open(f'/home/claude/castmate-pwa/public/icon-{size}.png', 'wb') as f:
        f.write(data)
    print(f"icon-{size}.png written ({len(data)} bytes)")
