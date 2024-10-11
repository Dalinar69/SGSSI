#FASE 1
from collections import Counter

# Letras más comunes en español, ordenadas de más a menos frecuentes
letras_comunes = 'EAOSRNIDLCTUMPBGYQVFHZJXW'

def descifrar_por_frecuencia(texto_cifrado):
    # Contar la frecuencia de cada letra en el texto cifrado
    contador = Counter(texto_cifrado.upper())
    
    # Ordenar las letras del texto cifrado de acuerdo a su frecuencia (más a menos frecuentes)
    letras_cifradas_ordenadas = [letra for letra, _ in contador.most_common() if letra.isalpha()]
    
    # Crear un diccionario para reemplazar cada letra cifrada con la más común del español
    reemplazo = {letras_cifradas_ordenadas[i]: letras_comunes[i] for i in range(len(letras_cifradas_ordenadas))}
    
    # Reemplazar las letras del texto cifrado con el nuevo mapeo
    texto_descifrado = ''.join(reemplazo.get(letra, letra) for letra in texto_cifrado.upper())
    
    return texto_descifrado

# Ejemplo de uso
texto_cifrado = """LC JGTIJGC D LC UTJIRLRFGC ECI JCBXGCVR TL BMIVR VT BCITKC VKCBCUGJC. C LR LCKFR VT LRW WGFLRW, TL AKRFKTWR JGTIUGNGJR EC UKCIWNRKBCVR IMTWUKCW PGVCW TI BMJERW CWATJURW, 
    VTWVT LC WCLMV ECWUC LC JRBMIGJCJGRI. LC GIPTIJGRI VT LC TLTJUKGJGVCV, LRW RKVTICVRKTW, D GIUTKITU ECI WGVR EGURW GBARKUCIUTW TI TWUT JCBGIR VT VTWCKKRLLR. 
    ERD, LC GIUTLGFTIJGC CKUGNGJGCL D LC CMURBCUGHCJGRI AKRBTUTI JCBXGCK CMI BCW IMTWUKR NMUMKR. WGI TBXCKFR, JRI TL CPCIJT KCAGVR PGTITI UCBXGTI FKCIVTW KTURW, JRBR TL JCBXGR JLGBCUGJR, 
    LC VTWGFMCLVCV UTJIRLRFGJC D LRW VTWCNGRW TUGJRW KTLCJGRICVRW JRI TL MWR VT IMTPCW UTJIRLRFGCW. TW NMIVCBTIUCL OMT LC WRJGTVCV CVRAUT MI TINROMT KTWARIWCXLT D WRWUTIGXLT NKTIUT C TWURW 
    VTWCNGRW, CWTFMKCIVR OMT TL AKRFKTWR JGTIUGNGJR D UTJIRLRFGJR XTITNGJGT C URVCW LCW ATKWRICW, WGI VTQCK C ICVGT CUKCW"""
texto_descifrado = descifrar_por_frecuencia(texto_cifrado)
print("\n")
print("Texto cifrado: ")
print("\n")
print(texto_cifrado)
print("\n") 
print("Texto descifrado por frecuencia: ")
print("\n")
print(texto_descifrado)
print("\n")
print("FIN DE LA FASE 1")
print("\n")

#FASE 2
def ordenar(letras):
    return sorted(letras.items(), key=lambda x: x[1], reverse=True)

def descifrar():
    mensaje = """LC JGTIJGC D LC UTJIRLRFGC ECI JCBXGCVR TL BMIVR VT BCITKC VKCBCUGJC. C LR LCKFR VT LRW WGFLRW, TL AKRFKTWR JGTIUGNGJR EC UKCIWNRKBCVR IMTWUKCW PGVCW TI BMJERW CWATJURW, 
    VTWVT LC WCLMV ECWUC LC JRBMIGJCJGRI. LC GIPTIJGRI VT LC TLTJUKGJGVCV, LRW RKVTICVRKTW, D GIUTKITU ECI WGVR EGURW GBARKUCIUTW TI TWUT JCBGIR VT VTWCKKRLLR. 
    ERD, LC GIUTLGFTIJGC CKUGNGJGCL D LC CMURBCUGHCJGRI AKRBTUTI JCBXGCK CMI BCW IMTWUKR NMUMKR. WGI TBXCKFR, JRI TL CPCIJT KCAGVR PGTITI UCBXGTI FKCIVTW KTURW, JRBR TL JCBXGR JLGBCUGJR, 
    LC VTWGFMCLVCV UTJIRLRFGJC D LRW VTWCNGRW TUGJRW KTLCJGRICVRW JRI TL MWR VT IMTPCW UTJIRLRFGCW. TW NMIVCBTIUCL OMT LC WRJGTVCV CVRAUT MI TINROMT KTWARIWCXLT D WRWUTIGXLT NKTIUT C TWURW 
    VTWCNGRW, CWTFMKCIVR OMT TL AKRFKTWR JGTIUGNGJR D UTJIRLRFGJR XTITNGJGT C URVCW LCW ATKWRICW, WGI VTQCK C ICVGT CUKCW
."""
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
    print("\n")
    

            
    mensajeReemplazado=mensaje
    
    mensajeReemplazado = mensajeReemplazado.replace("E", "H" )
    mensajeReemplazado = mensajeReemplazado.replace("T", "E" )
    mensajeReemplazado = mensajeReemplazado.replace("D", "Y" )
    mensajeReemplazado = mensajeReemplazado.replace("V", "D" )
    mensajeReemplazado = mensajeReemplazado.replace("P", "V" )
    mensajeReemplazado = mensajeReemplazado.replace("A", "P" )
    mensajeReemplazado = mensajeReemplazado.replace("C", "A" )
    mensajeReemplazado = mensajeReemplazado.replace("O", "Q" )
    mensajeReemplazado = mensajeReemplazado.replace("R", "O" )
    mensajeReemplazado = mensajeReemplazado.replace("K", "R" )
    mensajeReemplazado = mensajeReemplazado.replace("W", "S" )
    mensajeReemplazado = mensajeReemplazado.replace("U", "T" )
    mensajeReemplazado = mensajeReemplazado.replace("M", "U" )
    mensajeReemplazado = mensajeReemplazado.replace("B", "M" )
    mensajeReemplazado = mensajeReemplazado.replace("X", "B" )
    mensajeReemplazado = mensajeReemplazado.replace("J", "C" )
    mensajeReemplazado = mensajeReemplazado.replace("N", "v" )
    mensajeReemplazado = mensajeReemplazado.replace("I", "N" )
    mensajeReemplazado = mensajeReemplazado.replace("G", "I" )
    mensajeReemplazado = mensajeReemplazado.replace("F", "G" )
    mensajeReemplazado = mensajeReemplazado.replace("v", "F" )
    
    
    
    
    
  
       

    print(mensajeReemplazado)  


descifrar()

