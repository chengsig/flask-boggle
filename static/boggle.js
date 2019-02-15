$(document).ready(function(){
    let $makeGuessForm = $("#make_guess_form");
    let $guess = $("#guess")


    // get answer from form, make AJAX call to server
    $makeGuessForm.on("submit", async function(evt){
        console.log("it ran")
        evt.preventDefault();

        let guessedWord = $guess.val();

        await $.post("/hello", {"guess": guessedWord})
    })
})