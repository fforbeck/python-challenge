def conv(x):
    i = ord(x)
    if i < 121:
        return chr(i + 2)
    elif i == 121:
        return chr(ord('a'))
    elif i == 122:
        return chr(ord('b'))

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
chave = "".join(list(conv(k) for k in alfabeto))

texto = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb 
gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

print("===========  Tradução ============ \n")
print( texto.translate(str.maketrans(alfabeto, chave)))
print("===========  ======== ============ \n")



"""i hope you didnt translate it by hand.
thats what computers are for. doing it in by hand 
is inefficient and that's why this text is so long. 
using string.maketrans() is recommended. now apply on the url."""

print( "map".translate(str.maketrans(alfabeto, chave)))