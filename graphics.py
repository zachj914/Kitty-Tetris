import sys

from base64 import standard_b64encode

def serialize_gr_command(cmd, payload=None):
    cmd = ','.join('{}={}'.format(k, v) for k, v in cmd.items())
    ans = []
    w = ans.append
    w(b'\033_G'), w(cmd.encode('ascii'))
    if payload:
        w(b';')
        w(payload)
    w(b'\033\\')
    return b''.join(ans)

def write_chunked(cmd, data):
    data = standard_b64encode(data)
    while data:
        chunk, data = data[:4096], data[4096:]
        m = 1 if data else 0
        cmd['m'] = m
        sys.stdout.buffer.write(serialize_gr_command(cmd, chunk))
        sys.stdout.flush()
        cmd.clear()

def load_picture(Name, ID):
    with open(Name, 'rb') as f:
        write_chunked({'i': ID, 'f': 100}, f.read())

def move_cursor(line, column):
    sys.stdout.buffer.write(b'\033[%d;%dH' %(line, column))

def draw_piece(piece, x=0, y=0):
     move_cursor((y // 18) + 1, (x // 9) + 1)
     sys.stdout.buffer.write(serialize_gr_command(
        {'a': 'p', 'i': piece, 'X': x % 9, 'Y': y % 18}))
     move_cursor(0, 0)

def delete_piece(piece):
    sys.stdout.buffer.write(serialize_gr_command(
        {'a': 'd', 'd': 'i', 'i': piece}))

def refresh():
    sys.stdout.flush()

def clear_screen():
    sys.stdout.buffer.write(b'\033[2J')
    sys.stdout.flush()

