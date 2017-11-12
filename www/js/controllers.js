angular.module('app.controllers', ['ionic'])
  
.controller('loginCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$state', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope,$stateParams,$http,$localStorage,$location,$state) {


    if($localStorage.token){

      $location.url('page30')
    }

    function urlBase64Decode(str) {
        var output = str.replace('-', '+').replace('_', '/');
        switch (output.length % 4) {
            case 0:
                break;
            case 2:
                output += '==';
                break;
            case 3:
                output += '=';
                break;
            default:
                throw 'Illegal base64url string!';
        }
        return window.atob(output);
    }

    function getUserFromToken() {
        var token = $localStorage.token;
        var user = {};
        if (typeof token !== 'undefined') {
            var encoded = token.split('.')[1];
            user = JSON.parse(urlBase64Decode(encoded));
        }
        return user;
    }

    $scope.logeandose=0



    

    $scope.ingresar = function (data) {

         
          $scope.logeandose=1

           $http({

            url: 'http://xiencias.com:3000/api-token-auth/',
            data: data,
            method: 'POST'
            }).
            success(function(data) {

            console.log(data)
            
            $localStorage.token = data.token;

            var currentUser = getUserFromToken();

            if($localStorage.token){

                console.log('ingrese...')

                $location.url('page30')

                $scope.logeandose=0

                $scope.errors=''



            }


           })
            .error(function(data){

              console.log(data.errors.__all__)

              $scope.errors = data.errors.__all__

              $scope.logeandose=0


            })

    }

}])


// Adicionales Cointrollers
   
.controller('capitalCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$state','$ionicPopup', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller

function ($scope,$stateParams,$http,$localStorage,$location,$state,$ionicPopup) {




    $scope.setFile = function(element) {

    $scope.photo_1 = false

    $scope.statusimagen = 'Cargando imagen...'

    $scope.currentFile = element.files[0];


    var reader = new FileReader();

    reader.onload = function(event) {

    $scope.image = event.target.result

    $scope.$apply()

    }
    
    reader.readAsDataURL(element.files[0]);

    var file = $scope.myFile;

    var fd = new FormData();

    fd.append('file', $scope.currentFile);

    $http.post('http://xiencias.com:3000/uploadphoto/', fd, {
    transformRequest: angular.identity,
    headers: {'Content-Type': undefined}
    })
    

    .success(function(data){


      $http.get(host+"/agente/").success(function(response) {$scope.agente = response[0];});


    })



    }



    $scope.host= host

        $scope.okficha = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo datos correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         
      });    
   };

  
    


    $http.get(host+"/agente/").success(function(response) {$scope.agente = response[0];});
    $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});

    $scope.salir = function () {

      ionic.Platform.exitApp(); // para la aplicacion
    
      delete $localStorage.token;

      $location.path('/');

    }







 $scope.actualiza=function(data){


  $http({

            url: host+"/agente/",
            data: data,
            method: 'PUT'
            }).
            success(function(data) {

              $scope.okficha()

           })
 }



}])
   
.controller('agendaCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   

.controller('prospectoDeClienteCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicModal','$ionicPopup','$filter',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicModal,$ionicPopup,$filter) {


    $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});


    $ionicModal.fromTemplateUrl('templates/nuevocliente.html', {
      scope: $scope,
      animation: 'slide-in-up',
   }).then(function(modal) {
      $scope.nuevoclientemodal = modal;
   });

   $scope.nuevoclienteopenModal = function(data) {

    console.log(data)

      $scope.nuevoclientemodal.show();
   };
    
   $scope.nuevoclientecloseModal = function() {
      $scope.nuevoclientemodal.hide();
   };







/////////
    
     
  $ionicModal.fromTemplateUrl('templates/my-modal.html', {
      scope: $scope,
      animation: 'slide-in-up',
   }).then(function(modal) {
      $scope.modal = modal;
   });

   $scope.openModal = function(data) {

    console.log('abreeee...',data)

    $scope.propuesta = {}

    $scope.propuesta.cliente = data

      $scope.modal.show();
   };
    
   $scope.closeModal = function() {
      $scope.modal.hide();
   };
    
   //Cleanup the modal when we're done with it!
   $scope.$on('$destroy', function() {
      $scope.modal.remove();
   });
    
   // Execute action on hide modal
   $scope.$on('modal.hidden', function() {
      // Execute action
   });
    
   // Execute action on remove modal
   $scope.$on('modal.removed', function() {
      // Execute action
   });



  
       /// Popup



    $scope.okPropuestaPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo propuesta correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         $scope.closeModal()
      });    
   };

    $scope.okErrorPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Agente = Cliente ?',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         console.log('Tapped!', res);
      });    
   };

    $scope.okErrorEmail = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Este correo ya existe, porfavor ingrese otro correo',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         console.log('Tapped!', res);
      });    
   };





    $http.get(host+"/listaramos/").success(function(response) {$scope.ramos = response;});

     $http.get(host+"/clientes/").success(function(response) {$scope.todosclientes = response;});
    
     $scope.traetodoslosclientes = function(data){

        $http.get(host+"/clientes/").success(function(response) {$scope.todosclientes = response;});
    

    }

    $scope.searchb=false


    $scope.obtenercia = function(data){

       
        $http.get(host+"/listacia/"+data.id).success(function(response) {

            $scope.cias = response;});

    }

    $scope.traepropuestas = function(data){


      $http.get(host+"/listapropuestas/"+data).success(function(response) {

                  $scope.listapropuestas = response;




                  });

    }


    $scope.obtenerproducto = function(data){

    
         $http.get(host+"/listaproducto/"+$scope.propuesta.ramo.id+'/'+$scope.propuesta.cia).success(function(response) {

            $scope.productos = response;

            console.log('productos',response)

        });

    }

    $scope.agregacliente=function(data){


            $http({
            url: host+"/creacliente/",
            data: data,
            method: 'POST',

            }).
            success(function(data) {

              console.log('Guardo.....',data)


              if (data=='emailx'){

                $scope.okErrorEmail()
              }
              else{

                    $http.get(host+"/cliente/"+data).success(function(response) {

                    console.log(response[0])

                    $scope.clientesave = response[0];

                    });

                    $scope.nuevoclientemodal.hide()


              }





            })

    }

    ///Busca cliente

 
    $scope.traecliente=function(data){


      $http.get(host+"/cliente/"+data).success(function(response) {

                $scope.clientesave = response[0];

                $scope.todosclientes=''

                $scope.traepropuestas(data)

               


                

            });



    }

    $scope.agregapropuesta=function(data){


            console.log(data)



                  $http({
                  url: host+"/creapropuesta/",
                  data: data,
                  method: 'POST',

                  }).
                  success(function(data) {

                  console.log('fin..',data)
                  $scope.okPropuestaPopup()

                  $http.get(host+"/listapropuestas/"+data).success(function(response) {

                  $scope.listapropuestas = response;




                  });



                
            })

          

    }

   


}])
   

.controller('nuevaPropuestaCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup) {





}])
   
.controller('nuevaPropuestaSEGCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('pOSCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicModal','$ionicPopup','$ionicHistory','$filter',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicModal,$ionicPopup,$ionicHistory,$filter) {

    $scope.myGoBack = function() {
    $ionicHistory.goBack();
  };

  $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});

    $ionicModal.fromTemplateUrl('templates/nuevocliente.html', {
      scope: $scope,
      animation: 'slide-in-up',
   }).then(function(modal) {
      $scope.nuevoclientemodal = modal;
   });

   $scope.nuevoclienteopenModal = function(data) {

    console.log(data)

      $scope.nuevoclientemodal.show();
   };
    
   $scope.nuevoclientecloseModal = function() {
      $scope.nuevoclientemodal.hide();
   };


   $scope.creapos=function(data){

          data.tipo_cita=3
          data.cliente=$stateParams.cliente

          $http({
                  url: host+"/creapos/",
                  data: data,
                  method: 'POST',

                  }).
                  success(function(data) {

                    $scope.okCitaPopup()

                    // $location.url("/side-menu21/page19")

                    

    
               })


   }







/////////
    
     
  $ionicModal.fromTemplateUrl('templates/my-modal.html', {
      scope: $scope,
      animation: 'slide-in-up',
   }).then(function(modal) {
      $scope.modal = modal;
   });

   $scope.openModal = function(data) {

    console.log('abreeee...',data)

    $scope.propuesta = {}

    $scope.propuesta.cliente = data

      $scope.modal.show();
   };
    
   $scope.closeModal = function() {
      $scope.modal.hide();
   };
    
   //Cleanup the modal when we're done with it!
   $scope.$on('$destroy', function() {
      $scope.modal.remove();
   });
    
   // Execute action on hide modal
   $scope.$on('modal.hidden', function() {
      // Execute action
   });
    
   // Execute action on remove modal
   $scope.$on('modal.removed', function() {
      // Execute action
   });



  
       /// Popup


           $scope.okCitaPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo la cita correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {

        //$scope.myGoBack()

        //location.reload();
         
      });    
   };






    $scope.okPropuestaPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo propuesta correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         $scope.closeModal()
      });    
   };

       $scope.okErrorPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Agente = Cliente ?',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         console.log('Tapped!', res);
      });    
   };



    $http.get(host+"/listapropuestas/"+$stateParams.cliente).success(function(response) {


      $scope.productosdecliente = response;

      ///Filtrar productos activos

      $scope.productosdecliente=$filter('filter')($scope.productosdecliente,{"cierre" : 1})

      

      console.log('response',response)

    });


    $http.get(host+"/listaramos/").success(function(response) {$scope.ramos = response;});

     $http.get(host+"/clientes/").success(function(response) {$scope.todosclientes = response;});
    
     $scope.traetodoslosclientes = function(data){

        $http.get(host+"/clientes/").success(function(response) {$scope.todosclientes = response;});
    

    }

    $scope.searchb=false


    $scope.obtenercia = function(data){

       
        $http.get(host+"/listacia/"+data.id).success(function(response) {

            $scope.cias = response;});

    }

    $scope.traepropuestas = function(data){


      $http.get(host+"/listapropuestas/"+data).success(function(response) {

                  $scope.listapropuestas = response;




                  });

    }


    $scope.obtenerproducto = function(data){

    
         $http.get(host+"/listaproducto/"+$scope.propuesta.ramo.id+'/'+$scope.propuesta.cia).success(function(response) {

            $scope.productos = response;

            console.log('productos',response)

        });

    }

    $scope.agregacliente=function(data){


            $http({
            url: host+"/creacliente/",
            data: data,
            method: 'POST',

            }).
            success(function(data) {

              console.log('Guardo.....',data)



             $http.get(host+"/cliente/"+data).success(function(response) {

                $scope.clientesave = response[0];

                console.log(response[0])


            });

              $scope.nuevoclientemodal.hide()

            })

    }

    ///Busca cliente

 
    $scope.traecliente=function(data){


      $http.get(host+"/cliente/"+data).success(function(response) {

                $scope.clientesave = response[0];

                $scope.todosclientes=''

                $scope.traepropuestas(data)

               


                

            });



    }

    $scope.agregapropuesta=function(data){


            console.log(data)



                  $http({
                  url: host+"/creapropuesta/",
                  data: data,
                  method: 'POST',

                  }).
                  success(function(data) {

                  console.log('fin..',data)
                  $scope.okPropuestaPopup()

                  $http.get(host+"/listapropuestas/"+data).success(function(response) {

                  $scope.listapropuestas = response;

                  $scope.okCitaPopup()




                  });



                
            })

          

    }

   


}])
   
.controller('miPerfilCtrl', ['$scope','$stateParams','$http','$localStorage','$location', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location) {



    
 $http.get(host+"/agente/").success(function(response) {$scope.agente=response[0];});


 $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});
 


}])
   
.controller('introCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])


.controller('bibliotecaCtrl', ['$scope', '$stateParams','$http',// The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams,$http) {



    $http.get(host+"/losarchivos/").success(function(response) {$scope.archivos = response;


      console.log('hshsh',response)

    });


}])
   
.controller('seguimientoCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup','$ionicHistory', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup,$ionicHistory) {



    $scope.myGoBack = function() {
    $ionicHistory.goBack();
  };


    $scope.seguimiento=1
    $scope.cierre = 2
    $scope.poliza=2


    $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});
    $http.get(host+"/modalidad/").success(function(response) {$scope.modalidad = response;});

    $scope.okCitaPopup = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo la cita correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {

         
      });    
   };

    $scope.segui = {}


    $http.get(host+"/cliente/"+$stateParams.cliente).success(function(response) { 


      $scope.cliente = response[0];


    });


    console.log('$stateParams.propuesta',$stateParams.propuesta)


    if(!$stateParams.propuesta){

      
    console.log('entre..')

    $location.url("/page10")


    }


    $http.get(host+"/detallepropuesta/"+$stateParams.propuesta).success(function(response) { $scope.propuesta = response[0];});



    $scope.agregacita=function(data){

    

      $scope.segui={}

      $scope.segui.form = data
      $scope.segui.cliente = $stateParams.cliente
      $scope.segui.propuesta = $scope.propuesta

      $scope.segui.seguimiento=1

      console.log(data.prima_target)

      if (data.prima_target){

        $scope.segui.cierre=1
        $scope.segui.seguimiento=0
      
      }

      if (data.fecha_poliza){

        $scope.segui.poliza=1
        $scope.segui.seguimiento=0
      
      }


      // data.observacion=''
      // data.fecha_cita=''


      $http({
                  url: host+"/creacita/",
                  data: $scope.segui,
                  method: 'POST',

                  }).
                  success(function(data) {

                    $scope.okCitaPopup()

                    console.log('cita',data)



                    $location.url("/side-menu21/page19")





    
               })



    }

}])
   
.controller('clientesCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('seguimiento2Ctrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('creaCitaCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('alertaCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])


.controller('historialCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup','$filter', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup,$filter) {






$scope.reloadpage=function(){

  $http.get(host+"/citasagente/").success(function(response) { $scope.citas = response;console.log(response)});

}


$http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});


$http.get(host+"/citasagente/").success(function(response) { $scope.citas = response;console.log(response)});

$scope.iracita=function(data){



  $location.url("page20/"+data)
}

}])
   
.controller('citaCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup','$filter','$ionicHistory', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup,$filter,$ionicHistory) {



$http.get(host+"/citasagente/").success(function(response) { 

  $scope.citas = response;

  $scope.cita = $filter('filter')($scope.citas,{"id" : $stateParams.cita})[0]


});




$scope.updatecita = function(data){

  console.log(data)

   $http({
          url: host+"/updatecita/",
          data: data,
          method: 'POST',

          }).
          success(function(data) {

            console.log(data)


       })





}



$scope.eliminarcita = function(data){

  console.log(data)


    $http.get(host+"/eliminarcita/"+data.id).success(function(response) {

              
                $ionicHistory.goBack();

                  });






}



}])

  .controller('fichaDeClienteCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup','$ionicModal','$ionicHistory','$filter', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup,$ionicModal,$ionicHistory,$filter) {

  $scope.parientes={}


 


   $scope.myGoBack = function() {
    $ionicHistory.goBack();
  };

    $scope.okficha = function() {
      $scope.data = {}
    
      // Custom popup
      var myPopup = $ionicPopup.show({
         template: '',
         title: 'Se guardo datos correctamente',

         scope: $scope,
            
         buttons: [
            { text: 'Cerrar',type: 'button-light'}
         ]
      });

      myPopup.then(function(res) {
         $scope.closeModal()
      });    
   };

      $scope.closeModal = function() {
      $scope.modal.hide();
   };
    
   //Cleanup the modal when we're done with it!
   $scope.$on('$destroy', function() {
      $scope.modal.remove();
   });
    
   // Execute action on hide modal
   $scope.$on('modal.hidden', function() {
      // Execute action
   });
    
   // Execute action on remove modal
   $scope.$on('modal.removed', function() {
      // Execute action
   });



  $ionicModal.fromTemplateUrl('templates/parientes.html', {
      scope: $scope,
      animation: 'slide-in-up',
   }).then(function(modal) {
      $scope.modal = modal;



   });

   $scope.openModal = function(data) {

    

    $scope.id_cliente=data.id

    console.log('parientes...',$scope.parientes)

    $scope.propuesta = {}

    $scope.propuesta.cliente = data

      $scope.modal.show();
   };
    
   $scope.closeModal = function() {
      $scope.modal.hide();
   };
    
   //Cleanup the modal when we're done with it!
   $scope.$on('$destroy', function() {
      $scope.modal.remove();
   });
    
   // Execute action on hide modal
   $scope.$on('modal.hidden', function() {
      // Execute action
   });
    
   // Execute action on remove modal
   $scope.$on('modal.removed', function() {
      // Execute action
   });





    $http.get(host+"/listapropuestas/"+$stateParams.cliente).success(function(response) {

                  $scope.listapropuestas = response;

                  $scope.productosdecliente=$filter('filter')($scope.listapropuestas,{"cierre" : 1})


                  });



$scope.traecli = function(){

    $http.get(host+"/cliente/"+$stateParams.cliente).success(function(response) { 
    $scope.cliente = response[0];

    $scope.cliente.fecha_nacimiento=new Date($scope.cliente.fecha_nacimiento);


  });
}


$http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});

  $scope.traecli()

    $scope.edad=[]


    for (i = 0; i < 100; i++) { $scope.edad.push(i) } 

  $scope.agregapariente=function(data){

    $scope.hijos = []

    $scope.pariente={}

    data.cliente = $scope.id_cliente


     $http({
                  url: host+"/pariente/",
                  data: data,
                  method: 'POST',

                  }).
                  success(function(data) {

                    
                       $scope.traecli()
                       $scope.closeModal()
    
               })


 

    
  }

  $scope.actualizarcliente=function(data){

          $http({
                  url: host+"/creacliente/",
                  data: data,
                  method: 'PUT',

                  }).
                  success(function(data) {

                      console.log('atras')

                      $scope.okficha()

                      //$scope.myGoBack()
    
               })
  }


}])
   
.controller('registroDeCitasCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
  .controller('miGestionCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicPopup','$ionicModal','$ionicHistory', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicPopup,$ionicModal,$ionicHistory) {



  $http.get(host+"/gestion/").success(function(response) {$scope.gestion = response;

    console.log('gestion',response)

    $scope.produccionmensual =response.produccionmensual

    $scope.produccioncias = response.cias

    $scope.produccionramos = response.ramos


  });

}])
   
.controller('resumenDeNegociosCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('detalleNegocioCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {
    
    


}])
   


.controller('datosAdicionalesClienteCtrl', ['$scope','$stateParams','$http','$localStorage','$location', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location) {
    


}])
   
.controller('metricasCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$state','$filter', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller

function ($scope,$stateParams,$http,$localStorage,$location,$state,$filter) {


  $scope.mes =[
  {'id':1,'nombre':'Enero'},
  {'id':2,'nombre':'Febrero'},
  {'id':3,'nombre':'Marzo'},
  {'id':4,'nombre':'Abril'},
  {'id':5,'nombre':'Mayo'},
  {'id':6,'nombre':'Junio'},
  {'id':7,'nombre':'Julio'},
  {'id':8,'nombre':'Agosto'},
  {'id':9,'nombre':'Setiembre'},
  {'id':10,'nombre':'Octubre'},
  {'id':11,'nombre':'Noviembre'},
  {'id':12,'nombre':'Diciembre'}
  ]

  $scope.sacasemana =function(data){

    console.log(data)



    $http.get(host+"/calculo/"+data.numero).success(function(response) {$scope.calculo = response;

  console.log('calculo',response)


  
  });
  }


  $http.get(host+"/calculomes/").success(function(response) {$scope.calculomes = response;

  

  $scope.ncitasmes = JSON.parse(response.ncitasmes)

  $scope.nseguimientomes = JSON.parse(response.nseguimientomes)

  $scope.nposmes = JSON.parse(response.nposmes)

    });



$scope.sacames =function(data){



  console.log($scope.ncitasmes)


  $scope.ncmes=$filter('filter')($scope.ncitasmes,{"m" : data.id})

  $scope.nsmes=$filter('filter')($scope.nseguimientomes,{"m" : data.id})

  $scope.npmes=$filter('filter')($scope.nposmes,{"m" : data.id})


  console.log('sacames',$scope.ncmes)
    

  }




  $http.get(host+"/semanas/").success(function(response) {$scope.semanas = response;

  console.log('semanas',response)


  
  });

  $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});
  $http.get(host+"/termometro/").success(function(response) {$scope.termometro = response;

    console.log('termo',response)

    if (response.estado=='alerta'){

      $scope.colorestado='red'
    }
    else{

      $scope.colorestado='#0d49a0'
    }

     $scope.medida=response.porcentaje

     $scope.porcentajeesperado=response.porcentajeesperado

  });
  

  //Setiembre

 
  $http.get(host+"/metricas/09/04/09/08").success(function(response) { $scope.m090408 = response;console.log(response)});
  $http.get(host+"/metricas/09/11/09/15").success(function(response) { $scope.m091115 = response;console.log(response)});
  $http.get(host+"/metricas/09/18/09/23").success(function(response) { $scope.m091822 = response;console.log(response)});
  $http.get(host+"/metricas/09/25/09/29").success(function(response) { $scope.m092529 = response;console.log(response)});


  //Octubre
  
  $http.get(host+"/metricas/10/02/10/06").success(function(response) { $scope.m100206 = response;console.log(response)});
  $http.get(host+"/metricas/10/09/10/13").success(function(response) { $scope.m100913 = response;console.log(response)});
  $http.get(host+"/metricas/10/16/10/20").success(function(response) { $scope.m101620 = response;console.log(response)});
  $http.get(host+"/metricas/10/23/10/27").success(function(response) { $scope.m102327 = response;console.log(response)});
  $http.get(host+"/metricas/10/30/11/03").success(function(response) { $scope.m103003 = response;console.log(response)});


  //Noviembre

  $http.get(host+"/metricas/11/06/11/10").success(function(response) { $scope.m110610 = response;console.log(response)});
  $http.get(host+"/metricas/11/13/11/17").success(function(response) { $scope.m111317 = response;console.log(response)});
  $http.get(host+"/metricas/11/20/11/24").success(function(response) { $scope.m112024 = response;console.log(response)});
  $http.get(host+"/metricas/11/27/12/01").success(function(response) { $scope.m112701 = response;console.log(response)});


 //Diciembre

  $http.get(host+"/metricas/12/04/12/08").success(function(response) { $scope.m120408 = response;console.log(response)});
  $http.get(host+"/metricas/12/11/12/15").success(function(response) { $scope.m121115 = response;console.log(response)});
  $http.get(host+"/metricas/12/18/12/22").success(function(response) { $scope.m121822 = response;console.log(response)});
  $http.get(host+"/metricas/12/25/12/29").success(function(response) { $scope.m122529 = response;console.log(response)});




}])
   



.controller('propuestaSaludCtrl', ['$scope','$stateParams','$http','$localStorage','$location','$ionicHistory', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location,$ionicHistory) {


  console.log('$stateParams',$stateParams)

  $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});

  $scope.propuesta=$stateParams.propuesta


  $scope.eliminapropuesta = function(data){

      $http.get(host+"/eliminapropuesta/"+data).success(function(response) {

           location.reload();

             $ionicHistory.goBack();



                  });


  }


  $http.get(host+"/detallepropuesta/"+$scope.propuesta).success(function(response) {

                  $scope.detallepropuesta = response[0];





                  });




}])
   
.controller('misCierresCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('citaPOSCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('inicioCtrl', ['$scope','$stateParams','$http','$localStorage','$location', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope,$stateParams,$http,$localStorage,$location) {


    

    $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});


    $http.get(host+"/agente/").success(function(response) {$scope.agente = response[0];});


}])
   


  .controller('listaDePropuestasCtrl', ['$scope','$stateParams','$http','$localStorage','$location', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
function ($scope,$stateParams,$http,$localStorage,$location) {


      $scope.cliid =$stateParams.cliente

      $http.get(host+"/cliente/"+$stateParams.cliente).success(function(response) {

      console.log(response)

      $scope.clientepropuesta = response[0];

      $scope.traepropuestas($stateParams.cliente)

      });


    $http.get(host+"/iconos/").success(function(response) {$scope.iconos = response;});





      $scope.traepropuestas = function(data){


      $http.get(host+"/listapropuestas/"+data).success(function(response) {

                  $scope.listapropuestas = response;

                  console.log(response)




                  });

    }


}])
   
.controller('listaDePropuestasPOSCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
   
.controller('pagetestCtrl', ['$scope', '$stateParams', // The following is the constructor function for this page's controller. See https://docs.angularjs.org/guide/controller
// You can include any angular dependencies as parameters for this function
// TIP: Access Route Parameters for your page via $stateParams.parameterName
function ($scope, $stateParams) {


}])
 