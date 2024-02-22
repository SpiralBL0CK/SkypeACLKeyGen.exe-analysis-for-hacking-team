import hashlib

path = "C:\\Users"
binar = b"4141".decode('utf-8') #open()
s =  "Element'ry!penguiNs;-)SingingHareKrishna_"
tmp = path.upper().encode('utf-8')+s.encode('utf-8')
tmp2 = (str(binar)+s).encode('utf-8')
key1 = str(
    hashlib.md5(
        str(
            hashlib.md5(
                tmp).hexdigest() ).encode('utf-8') ).hexdigest()) + str(hashlib.md5(str(hashlib.md5(tmp2).hexdigest()).encode('utf-8')).hexdigest())

z = "Per"+s.upper()+"mit"
key2 = str(hashlib.md5(z.encode('utf-8')).hexdigest())
key3 = str(hashlib.md5("0".encode('utf-8')).hexdigest())
final_string = ""
final_string += "<AccessControlList>"
final_string += "\n"
final_string += "\r\t\t<Key1>{}</Key1>\n".format(key1)
final_string += "\r\t\t<Key2>{}</Key2>\n".format(key2)
final_string += "\r\t\t<Key3>{}</Key3>\n".format(key3)
final_string += "\r</AccessControlList>\n"
print(final_string)

    