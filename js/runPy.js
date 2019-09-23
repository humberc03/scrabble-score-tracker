$.ajax({
  type: "POST",
  url: "../main.py",
  data: { param: text}
}).done(function( o ) {
   // do something
});

// could be used to run the python program? more likely php via apache or github's hosting
