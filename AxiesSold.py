import json
import requests
from axie_functions import lista_add, index_list



#AXIE CLASSES :

  
axieclass_list = ['aquatic','beast','bird','bug','plant','reptile','dusk','dawn','mech']


#AXIE PARTS :

axieeyes_list = ["Clear", "Gero","Sleepless",'Telescope','Flower Sunglasses','Chubby','Little Peas','Puppy', 'Zeal','Little Owl', 'Lucas', 'Mavis', 'Robin', 'Bookworm', 'Kotaro?','Neo','Nerdy', 'Blossom', 'Confused', 'Cucumber Slice','Papi','Gecko','Scar','Topaz','Tricky']
axieears_list = ['Bubblemaker','Gill','Inkling','Nimo','Seaslug','Tiny Fan','Belieber','Coca','Innocent Lamb','Nut Cracker','Nyan','Puppy','Zen','Curly','Early Bird', 'Owl','Peace Maker','Pink Cheek','Risky Bird','Beetle Spike','Ear Breathing','Earwing' ,'Larva','Leaf Bug','Tassels','Clover','Hollow','Leafy','Lotus','Rosa','Sakura','Curved Spine','Friezard','Pogona','Sidebarb','Small Frill','Swirl']
axiehorn_list =['Anemone','Babylonia','Clamshell','Oranda','Shoal Star','Teal Shell','Arco','Dual Blade','Imp','Little Branch','Merry','Pocky','Cuckoo','Eggshell','Feather Spear','Kestrel','Trump','Wing Horn','Antenna','Caterpillars','Lagging','Leaf Bug','Parasite','Pliers','Bamboo Shoot','Beech','Cactus','Rose Bud','Strawberry Shortcake','Watermelon','Bumpy','Cerastes','Incisor','Watermelon Ice Cream','Scaly Spear','Scaly Spoon','Unko','Strawberry Ice Cream']
axieback_list = ['Anemone','Blue Moon','Goldfish','Hermit','Perch','Sponge','Furball','Beach Ball','Hero','Jaguar','Risky Beast','Ronin','Timber','Balloon','Cupid','Kingfisher','Pigeon Post','Raven','Tri Feather','Buzz Buzz','Garish Worm','Sandal','Scarab','Snail Shell','Spiky Wing','Bidens','Mint','Pumpkin','Shiitake','Succulent','Turnip','Watering Can','Bone Sail','Croc','Green Thorns','Turtle Buoy','Indian Star','Red Ear','Tiny Dino','Tri Spikes']
axiemouth_list = ['Catfish','Lam','Piranha','Risky Fish','Axie Kiss','Confident','Goda','Nut Cracker','Doubletalk','Hungry Bird','Little Owl','Peace Maker','Cute Bunny','Mosquito','Pincer','Square Teeth','Herbivore','Serious','Silence Whisper','Zigzag','Kotaro','Razor Bite','Tiny Turtle','Toothless Bite']
axietail_list = ['Koi','Navaga','Nimo','Ranchu','Shrimp','Tadpole','Cottontail','Gerbil','Hare','Cotton Candy','Nut Cracker','Rice','Shiba','Cloud','Feather Fan',"Granma's Fan",'Post Fight','Swallow','The Last One','Ant','Fish Snack','Gravel Ant','Pupae','Thorny Caterpillar','Twin Tail','Carrot','Cattail','Hatsune','Hot Butt','Potato Leaf','Yam','Gila','Grass Snake','Iguana','Snake Jar','Tiny Dino','Wall Gecko']

axie_parts_list = [axieeyes_list,axieears_list,axiehorn_list,axieback_list,axiemouth_list,axietail_list] # LISTA DE PARTES COMPLETA


#FUNCION : CREACION CONTADOR DE PARTES POR TIPO (EYES, MOUTH, ETC) LIGADO A SU LISTA DE PARTES

axieclass_add = lista_add(axieclass_list)

#LISTA DE LISTA DE CONTEOS 'ADD_LISTS'

add_parts_list = [lista_add(axieeyes_list),lista_add(axieears_list),lista_add(axiehorn_list),lista_add(axieback_list),lista_add(axiemouth_list),lista_add(axietail_list)]
"""eyes_add = lista_add(axieeyes_list)
ears_add = lista_add(axieears_list)
horn_add = lista_add(axiehorn_list)
back_add = lista_add(axieback_list)
mouth_add = lista_add(axiemouth_list)
tail_add = lista_add(axietail_list)"""


#print(axieclass_add) # REVISAR TOTAL DE ELEMENTOS EN LISTA
#print(ears_add)





infoaxiejson = '''
{
  "operationName": "GetRecentlyAxiesSold",
  "variables": {
    "from": 0,
    "size": 10
  },
  "query": "query GetRecentlyAxiesSold($from: Int, $size: Int) {\n  settledAuctions {\n    axies(from: $from, size: $size) {\n      total\n      results {\n        ...AxieSettledBrief\n        transferHistory {\n          ...TransferHistoryInSettledAuction\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment AxieSettledBrief on Axie {\n  id\n  name\n  image\n  class\n  breedCount\n  __typename\n}\n\nfragment TransferHistoryInSettledAuction on TransferRecords {\n  total\n  results {\n    ...TransferRecordInSettledAuction\n    __typename\n  }\n  __typename\n}\n\nfragment TransferRecordInSettledAuction on TransferRecord {\n  from\n  to\n  txHash\n  timestamp\n  withPrice\n  withPriceUsd\n  fromProfile {\n    name\n    __typename\n  }\n  toProfile {\n    name\n    __typename\n  }\n  __typename\n}\n"
}
'''


infoaxie = json.loads(infoaxiejson, strict=False)

#BUSCANDO VENTAS ///// WHILE ANTES DEL REQUEST DE DETALLES PARA PODER ACTUALIZAR RESULTADO 
a=0
##i = 0
while a <= 100 :
  #i = 0
 ## a += 1
#print(axiedetailsjson)
  respuesta = requests.get('https://graphql-gateway.axieinfinity.com/graphql', infoaxie)


  resultado = json.loads(respuesta.text) ## TRANSFORMANDO RESPUESTA EN DICCIONARIO PHYTON


  # IMPRESION ORDENADA DE LA PRIMERA RESPUESTA

  #axieinfojson = json.dumps(resultado,indent=2) # /// PRUEBA DE ORGANIZACION

  #print(axieinfojson)  # IMPRESION ORDENADA DE LA PRIMERA RESPUESTA


  


  
  for v in resultado['data']['settledAuctions']['axies']['results']:#['name']: #INDEX DATOS RETORNADOS #['data']   ['settledAuctions']['axies'] 
      #print(v['id'])
      axieId = v['id']
      #print(v['name'])


      getaxie = 'https://ronin.rest/ronin/axie/'

      getaxie += axieId

      respuestaId = requests.get(getaxie) #RESPUESTA JSON

      #print(respuestaId)

      details_id = json.loads(respuestaId.text) #RESPUESTA EN DICCIONARIO

      #respuestaId2 = json.dumps(detailsperId, indent=2)

      #print(respuestaId2)   #MOSTRAR LA RESPUESTA DEL servidor 'DETALLES AXIE' ////

     #VERIFICAR RESPUESTA PARA CONFIRMAR INDEX

      

      axie_class = details_id["genes"]["cls"]

      def axiepart_f (axiepart_) :

        return details_id["genes"][axiepart_]["d"]["name"]

      respuesta_details_list = [ axiepart_f("eyes"),axiepart_f("ears"),axiepart_f("horn"),axiepart_f("back"),axiepart_f("mouth"),axiepart_f("tail")]

      #print(respuesta_details_list)


     
      

      for i in range(len(respuesta_details_list)) :

        #print(respuesta_details_list)

        index_add_list = index_list(axie_parts_list[i],respuesta_details_list[i])

        add_parts_list[i][index_add_list] += 1

        print(add_parts_list)


      #FUNCION DETECCION INDEX DE CLASE DE AXIE VENDIDO Y SUMANDOLO EN LISTA ADD PARA DAR RESULTADO DE VENTAS


  """

   # print(max(axieClassAdd))

 

    #ESTOY MOSTRANDO LAS ESTADISTICAS POR CADA RESPUESTA (ULTIMOS20 AXIES)

    #RESSULTADO SE ACUMULA Y VA SIENDO MAS PRECISO


  print('Clase Numero 1 en Ventas :',axieclass_list[axieclass_add.index(max(axieclass_add))])#f.write(axieClassList[axieClassAdd.index(max(axieClassAdd))]) #UTILIZO EL INDICE DEL MAXIMO VALOR EN
                                                                #EN LA LISTA 'axieClassAdd' PARA ENCONTRAR
                                                                #EL NOMBRE DE LA ESPECIE MAS VENDIDA EN LA LISTA 'axieClassAdd'
  
  
  #f.write(axieEyesList[eyesAdd.index(max(eyesAdd))])

  #UTILIZO EL INDICE DEL MAXIMO VALOR EN
  #EN LA LISTA 'eyesAdd' PARA ENCONTRAR
  #EL NOMBRE DEL 'EYES' MAS VENDIDA EN LA LISTA 'eyesAdd'


  print('Eyes Numero 1 en Ventas:' ,axieeyes_list[eyes_add.index(max(eyes_add))]) 

  
  print('Ears Numero 1 en Ventas:' ,axieears_list[ears_add.index(max(ears_add))]) 


  print('Horn Numero 1 en Ventas:' ,axiehorn_list[horn_add.index(max(horn_add))]) 


  print('Back Numero 1 en Ventas:' ,axieback_list[back_add.index(max(back_add))]) 


  print('Mouth Numero 1 en Ventas:' ,axiemouth_list[mouth_add.index(max(mouth_add))]) 


  print('Tail Numero 1 en Ventas:' ,axietail_list[tail_add.index(max(tail_add))]) 




# AQUI IMPRIMO EL SEGUNDO MAS VENDIDO :
 axieClassList2 = axieClassList[:]     #COPIADO DE LISTAS PARA ELIMINAR ELEMENTOS DEL INDICE DEL MAYOR ELEMENTO
                                      #PARA MOSTRAR EL SEGUNDO MAYOR ELEMENTO
  axieClassAdd2 = axieClassAdd[:]


  axieEyesList2 = axieEyesList[:]

  eyesAdd2 = eyesAdd[:]




  axieClassList2.pop(axieClassAdd.index(max(axieClassAdd)))  

  axieClassAdd2.pop(eyesAdd.index(max(eyesAdd)))

  axieEyesList2.pop(axieClassAdd.index(max(axieClassAdd)))

  eyesAdd2.pop(eyesAdd.index(max(eyesAdd)))



  print('Clase Numero 2 en Ventas :',axieClassList2[axieClassAdd2.index(max(axieClassAdd2))])

  print('Eyes Numero 2 en Ventas:' ,axieEyesList2[eyesAdd2.index(max(eyesAdd2))]  )
  

#print(eyesAdd)
#print(axieClassAdd)    #VERIFICANDO RESULTADOS IMPRIMIENTO LISTAS """




