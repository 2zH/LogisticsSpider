angular.module('SupportApp', ['ngMaterial'])

.config(function($mdThemingProvider){
  $mdThemingProvider.theme('altTheme')
  .primaryPalette('purple');
})

.controller('SubheaderAppCtrl', function($scope){
  var imagePath = 'img/1.jpg';
  $scope.messages = [
    {
      face: 'img/2.jpg',
      address: '贵安校区',
      man: '沈泽禾',
      when: '3:08PM',
      content: " 测试"
    },
  ];
});
