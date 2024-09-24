def ordenar(letras):
    return sorted(letras.items(), key=lambda x: x[1], reverse=True)

def descifrar():
    mensaje = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""
    letras = {
        "A" : 0,
        "B" : 0,
        "C" : 0,
        "D" : 0,
        "E" : 0,
        "F" : 0,
        "G" : 0,
        "H" : 0,
        "I" : 0,
        "J" : 0,
        "K" : 0,
        "L" : 0,
        "M" : 0,
        "N" : 0,
        "O" : 0,
        "P" : 0,
        "Q" : 0,
        "R" : 0,
        "S" : 0,
        "T" : 0,
        "U" : 0,
        "V" : 0,
        "W" : 0,
        "X" : 0,
        "Y" : 0,
        "Z" : 0
    }
    for char in mensaje:
        if char in letras:
            letras[char] += 1
    letras= ordenar(letras)       
    print(letras)
    

            
    mensajeReemplazado=mensaje
    mensajeReemplazado = mensajeReemplazado.replace("Q", "B" )
    mensajeReemplazado = mensajeReemplazado.replace("S", "Q" )
    mensajeReemplazado = mensajeReemplazado.replace("N", "S" )
    mensajeReemplazado = mensajeReemplazado.replace("J", "N" )
    mensajeReemplazado = mensajeReemplazado.replace("G", "J" )
    mensajeReemplazado = mensajeReemplazado.replace("U", "G" )
    mensajeReemplazado = mensajeReemplazado.replace("Z", "U" )
    mensajeReemplazado = mensajeReemplazado.replace("L", "Z" )
    mensajeReemplazado = mensajeReemplazado.replace("T", "L" )
    mensajeReemplazado = mensajeReemplazado.replace("H", "T" )
    mensajeReemplazado = mensajeReemplazado.replace("M", "H" )
    mensajeReemplazado = mensajeReemplazado.replace("P", "M" )
    mensajeReemplazado = mensajeReemplazado.replace("D", "P" )
    mensajeReemplazado = mensajeReemplazado.replace("A", "D" )
    mensajeReemplazado = mensajeReemplazado.replace("E", "A" )
    mensajeReemplazado = mensajeReemplazado.replace("X", "E" )
    mensajeReemplazado = mensajeReemplazado.replace("F", "X" )
    mensajeReemplazado = mensajeReemplazado.replace("O", "F" )
    mensajeReemplazado = mensajeReemplazado.replace("I", "O" )
    mensajeReemplazado = mensajeReemplazado.replace("C", "I" )
    mensajeReemplazado = mensajeReemplazado.replace("R", "C" )
    mensajeReemplazado = mensajeReemplazado.replace("K", "R" )
    mensajeReemplazado = mensajeReemplazado.replace("V", "Y" )
    mensajeReemplazado = mensajeReemplazado.replace("v", "V" )
    
    
    
  
       

    print(mensajeReemplazado)  


descifrar()

