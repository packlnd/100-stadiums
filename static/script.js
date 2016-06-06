$(function() {
  $("img").on("click", function() {
    alert($(this).closest("div").attr("id"));
  });
});
