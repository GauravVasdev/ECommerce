$(document).ready(function(){
	$(".womenwatchpic").hover(function(){
    //$(this).css("background-color", "yellow");
    	$(this).find(".btnelement").show();
    }, function(){
    	$(this).find(".btnelement").hide();
  	});
	$(".btnelement").hover(function(){
		$(this).css({"background-color":"white","color":"black"});
	},function(){
		$(this).css({"background-color":"rgba(0,0,0,0.5)","color":"white"});
	});
	$(".backbtn").hover(function(){
      $(".bchtext").show();
    },function(){
      $(".bchtext").hide();
    });
    // $(".backbtn").click(function(){
    //   window.location.href="../../Home.html";
    // });
});