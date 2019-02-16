$(document).ready(function(){
    let $makeGuessForm = $("#make_guess_form");
    let $guess = $("#guess");
    let $showResult = $("#show_result");
    let $showScore = $("#show_score");
    let totalScore = 0;
    let button_state = true;    


    // get answer from form, make AJAX call to server
    $makeGuessForm.on("submit", async function(evt){
        evt.preventDefault();

        if(button_state){

            let guessedWord = $guess.val();

            response = await $.post("/", {"guess": guessedWord});
            
            if(response.result === "ok"){
                totalScore += guessedWord.length;
            }

            $showResult.text(`Your word is ${response.result}`);
            $showScore.text(`Total score: ${totalScore}`);

            $guess.val("");
        }

        setTimeout(function(){
            alert("time up!");
            button_state = false;
        }, 8000);

    })

})