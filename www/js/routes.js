angular.module('app.routes', ['ngStorage'])

.directive('fileModel', ['$parse', function ($parse) {
            return {
               restrict: 'A',
               link: function(scope, element, attrs) {
                  var model = $parse(attrs.fileModel);
                  var modelSetter = model.assign;
                  
                  element.bind('change', function(){
                     scope.$apply(function(){
                        modelSetter(scope, element[0].files[0]);
                     });
                  });
               }
            };
         }])

.config(function($stateProvider, $urlRouterProvider,$httpProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    

    .state('login', {
      url: '/page1',
      templateUrl: 'templates/login.html',
      controller:'loginCtrl'
    })
        .state('capital', {
      url: '/side-menu21',
      templateUrl: 'templates/capital.html',
      controller:'capitalCtrl'
    })
        .state('agenda', {
      url: '/page4',
      templateUrl: 'templates/agenda.html',
      controller:'loginCtrl'
    })
        .state('prospectoDeCliente', {
      url: '/page5',
      templateUrl: 'templates/prospectoDeCliente.html',
      controller:'prospectoDeClienteCtrl'
    })
        .state('nuevaPropuesta', {
      url: '/page14',
      templateUrl: 'templates/nuevaPropuesta.html',
      controller:'nuevaPropuestaCtrl'
    })
        .state('nuevaPropuestaSEG', {
      url: '/page31',
      templateUrl: 'templates/nuevaPropuestaSEG.html',
      controller:'loginCtrl'
    })
        .state('pOS', {
      url: '/page16',
      templateUrl: 'templates/pOS.html',
      controller:'prospectoDeClienteCtrl'
    })
    
    .state('capital.miPerfil', {
      url: '/page11',
      views: {
        'side-menu21': {
          templateUrl: 'templates/miPerfil.html',
          controller:'capitalCtrl'
        }
      }
    })
        .state('intro', {
      url: '/page9',
      templateUrl: 'templates/intro.html',
      controller:'loginCtrl'
    })
        .state('seguimiento', {
      url: '/page10',
      templateUrl: 'templates/seguimiento.html',
      controller:'prospectoDeClienteCtrl'
    })
        .state('capital.clientes', {
      url: '/page22',
      views: {
        'side-menu21': {
          templateUrl: 'templates/clientes.html',
          controller:'prospectoDeClienteCtrl'
        }
      }
    })
        .state('seguimiento2', {
      url: '/page13',
      templateUrl: 'templates/seguimiento2.html',
      controller:'seguimientoCtrl',
      params: {
        cliente: null,
        propuesta:null
      }
    })
        .state('creaCita', {
      url: '/page12',
      templateUrl: 'templates/creaCita.html',
      controller:'loginCtrl'
    })
        .state('alerta', {
      url: '/page18',
      templateUrl: 'templates/alerta.html',
      controller:'loginCtrl'
    })
        .state('capital.historial', {
      url: '/page19',
      views: {
        'side-menu21': {
          templateUrl: 'templates/historial.html',
          controller:'historialCtrl'
        }
      }
    })
      .state('capital.biblioteca', {
      url: '/biblioteca',
      views: {
        'side-menu21': {
          templateUrl: 'templates/biblioteca.html',
          controller:'bibliotecaCtrl'
        }
      }
    })
        .state('cita', {
      url: '/page20',
      templateUrl: 'templates/cita.html',
      controller:'citaCtrl',
      params: {
        cita: null
      }
    })
        .state('fichaDeCliente', {
      url: '/page15',
      templateUrl: 'templates/fichaDeCliente.html',
      controller:'fichaDeClienteCtrl',
       params: {
        cliente: null
      }
    })
        .state('capital.registroDeCitas', {
      url: '/page21',
      views: {
        'side-menu21': {
          templateUrl: 'templates/registroDeCitas.html',
          controller:'loginCtrl'
        }
      }
    })
        .state('capital.miGestion', {
      url: '/page24',
      views: {
        'side-menu21': {
          templateUrl: 'templates/miGestion.html',
          controller:'miGestionCtrl'
        }
      }
    })
        .state('capital.resumenDeNegocios', {
      url: '/page26',
      views: {
        'side-menu21': {
          templateUrl: 'templates/resumenDeNegocios.html',
          controller:'loginCtrl'
        }
      }
    })

 
        .state('datosAdicionalesCliente', {
      url: '/page17',
      templateUrl: 'templates/datosAdicionalesCliente.html',
      controller:'loginCtrl'
    })
        .state('capital.metricas', {
      url: '/page23',
      views: {
        'side-menu21': {
          templateUrl: 'templates/metricas.html',
          controller:'metricasCtrl'
        }
      }
    })
        .state('propuestaSalud', {
      url: '/page25',
      templateUrl: 'templates/propuestaSalud.html',
      controller:'propuestaSaludCtrl',
      params: {
        propuesta: null
      }
    })
        .state('capital.misCierres', {
      url: '/page28',
      views: {
        'side-menu21': {
          templateUrl: 'templates/misCierres.html',
          controller:'loginCtrl'
        }
      }
    })
        .state('citaPOS', {
      url: '/page29',
      templateUrl: 'templates/citaPOS.html',
      controller:'pOSCtrl',
      params: {
        cliente: null
      }
    })
        .state('inicio', {
      url: '/page30',
      templateUrl: 'templates/inicio.html',
      controller:'capitalCtrl'
    })
        .state('listaDePropuestas', {
      url: '/page32',
      templateUrl: 'templates/listaDePropuestas.html',
      controller:'listaDePropuestasCtrl',
      params: {
        cliente: null
      }
    })




        .state('listaDePropuestasPOS', {
      url: '/page34',
      templateUrl: 'templates/listaDePropuestasPOS.html',
      controller:'loginCtrl'
    })
        .state('pagetest', {
      url: '/page33',
      templateUrl: 'templates/pagetest.html',
      controller:'loginCtrl'
    })
    ;

  // if none of the above states are matched, use this as the fallback
  $urlRouterProvider.otherwise('/page1');

  host =  "http://xiencias.com:3000"

  //Django Auth JWT 

  $httpProvider.defaults.headers.post['Accept'] = 'application/json, text/javascript'; 

  $httpProvider.defaults.headers.post['Content-Type'] = 'multipart/form-data; charset=utf-8';


  $httpProvider.interceptors.push(['$q', '$location', '$localStorage', function($q, $location, $localStorage) {
        return {
                'request': function (config) {
                    config.headers = config.headers || {};
                    if ($localStorage.token) {
                        config.headers.Authorization = 'Bearer ' + $localStorage.token;
                    }
                    return config;
                },
                'responseError': function(response) {
                    if(response.status === 401 || response.status === 403) {
                        $location.path('/signin');
                    }
                    return $q.reject(response);
                }
            };
        }]);



  


});