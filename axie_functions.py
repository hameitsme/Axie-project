def lista_add(axiepart_list) : # CREANDO LISTAS EN CERO EQUIVALENTES A LISTA DE PARTES PARA CONTEO
  
    part_list_add = [0 for i in axiepart_list]

    return part_list_add



def index_list (axie_parts_list,respuesta_details_list) : #BUSCANDO INDICE DE CADA RESPUESTA "respuesta_details_list"
                                                                #EN LA LISTA "print(axie_parts_list"
    #print(axie_parts_list)
    print(axie_parts_list.index(respuesta_details_list))

    return axie_parts_list.index(respuesta_details_list)



def parts_from_id (axiepart_,details_id) :          #OBTENGO CADA PARTE DEL AXIE A PARTIR DE SU "ID"

        return details_id["genes"][axiepart_]["d"]["name"]