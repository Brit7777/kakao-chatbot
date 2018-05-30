var requestLoop = setInterval(function(){
  request({
      url: "https://mighty-spire-71391.herokuapp.com",
      method: "GET",
      timeout: 10000,
      followRedirect: true,
      maxRedirects: 10
  },function(error, response, body){
      if(!error && response.statusCode == 200){
          console.log('sucess!');
      }else{
          console.log('error' + response.statusCode);
      }
  });
}, 60000);
