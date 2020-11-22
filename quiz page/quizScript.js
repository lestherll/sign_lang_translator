var questions = [
    {
        question : "signs/A.png",
        choiceA : "A",
        choiceB : "Z",
        choiceC : "W",
        choiceD : "G",
        correct : "A"
    },
    {
        question : "signs/B.png",
        choiceA : "H",
        choiceB : "S",
        choiceC : "D",
        choiceD : "B",
        correct : "D"
    },
    {
        question : "signs/C.png",
        choiceA : "G",
        choiceB : "C",
        choiceC : "E",
        choiceD : "O",
        correct : "B"
    },
    {
        question : "signs/D.png",
        choiceA : "O",
        choiceB : "J",
        choiceC : "D",
        choiceD : "N",
        correct : "C"
    },
    {
        question : "signs/E.png",
        choiceA : "G",
        choiceB : "D",
        choiceC : "E",
        choiceD : "T",
        correct : "C"
    },
    {
        question : "signs/F.png",
        choiceA : "H",
        choiceB : "S",
        choiceC : "G",
        choiceD : "F",
        correct : "D"
    },
    {
        question : "signs/G.png",
        choiceA : "C",
        choiceB : "G",
        choiceC : "O",
        choiceD : "L",
        correct : "B"
    },
    {
        question : "signs/H.png",
        choiceA : "D",
        choiceB : "H",
        choiceC : "T",
        choiceD : "K",
        correct : "B"
    },
    {
        question : "signs/I.png",
        choiceA : "J",
        choiceB : "I",
        choiceC : "Z",
        choiceD : "V",
        correct : "B"
    },
    {
        question : "signs/J.png",
        choiceA : "X",
        choiceB : "B",
        choiceC : "J",
        choiceD : "T",
        correct : "C"
    },
    {
        question : "signs/K.png",
        choiceA : "X",
        choiceB : "G",
        choiceC : "F",
        choiceD : "K",
        correct : "D"
    },
    {
        question : "signs/L.png",
        choiceA : "D",
        choiceB : "L",
        choiceC : "B",
        choiceD : "U",
        correct : "B"
    },
    {
        question : "signs/M.png",
        choiceA : "U",
        choiceB : "W",
        choiceC : "M",
        choiceD : "N",
        correct : "C"
    },
    {
        question : "signs/N.png",
        choiceA : "N",
        choiceB : "R",
        choiceC : "T",
        choiceD : "S",
        correct : "A"
    },
    {
        question : "signs/O.png",
        choiceA : "Y",
        choiceB : "Q",
        choiceC : "C",
        choiceD : "O",
        correct : "D"
    },
    {
        question : "signs/P.png",
        choiceA : "P",
        choiceB : "Q",
        choiceC : "F",
        choiceD : "L",
        correct : "A"
    },
    {
        question : "signs/Q.png",
        choiceA : "Q",
        choiceB : "O",
        choiceC : "P",
        choiceD : "Y",
        correct : "A"
    },
    {
        question : "signs/R.png",
        choiceA : "H",
        choiceB : "B",
        choiceC : "V",
        choiceD : "R",
        correct : "D"
    },
    {
        question : "signs/S.png",
        choiceA : "W",
        choiceB : "S",
        choiceC : "Z",
        choiceD : "J",
        correct : "B"
    },
    {
        question : "signs/T.png",
        choiceA : "T",
        choiceB : "W",
        choiceC : "D",
        choiceD : "J",
        correct : "A"
    },
    {
        question : "signs/U.png",
        choiceA : "W",
        choiceB : "V",
        choiceC : "U",
        choiceD : "Y",
        correct : "C"
    },
    {
        question : "signs/V.png",
        choiceA : "N",
        choiceB : "V",
        choiceC : "M",
        choiceD : "S",
        correct : "B"
    },
    {
        question : "signs/W.png",
        choiceA : "M",
        choiceB : "W",
        choiceC : "N",
        choiceD : "U",
        correct : "B"
    },
    {
        question : "signs/X.png",
        choiceA : "S",
        choiceB : "A",
        choiceC : "Z",
        choiceD : "X",
        correct : "D"
    },
    {
        question : "signs/Y.png",
        choiceA : "A",
        choiceB : "S",
        choiceC : "Y",
        choiceD : "J",
        correct : "C"
    },
    {
        question : "signs/Z.png",
        choiceA : "L",
        choiceB : "Z",
        choiceC : "B",
        choiceD : "S",
        correct : "B"
    }
];

var score = 0;
var count = 0;
var timer;
var currentQuestion = 0;

const questionsPerQuiz = 10;
const maxTime = 60; 

const beginButton = document.getElementById("begin");
const quiz = document.getElementById("quiz");
const question = document.getElementById("question");
const questionNumber = document.getElementById("questionNumber");
const choiceA = document.getElementById("A");
const choiceB = document.getElementById("B");
const choiceC = document.getElementById("C");
const choiceD = document.getElementById('D');
const countdown = document.getElementById("countdown");
const scoreDiv = document.getElementById("score");

function shuffle(array) 
{
    var currentIndex = array.length;
    var temporaryValue;
    var randomIndex;
  
    while (0 !== currentIndex) 
    {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex --;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}

shuffle(questions);

function begin()
{
    beginButton.style.display = "none";
    quiz.style.display = "block";
    questionNumber.style.display = "inline"

    showQuestion();

    choiceA.style.display = "inline-block";
    choiceB.style.display = "inline-block";
    choiceC.style.display = "inline-block";
    choiceD.style.display = "inline-block";

    showCountdown();
    timer = setInterval(showCountdown,1000);
}

function showQuestion()
{
    var q = questions[currentQuestion];
    
    question.innerHTML = "<img src="+ q.question +">";
    choiceA.innerHTML = q.choiceA;
    choiceB.innerHTML = q.choiceB;
    choiceC.innerHTML = q.choiceC;
    choiceD.innerHTML = q.choiceD;

    questionNumber.innerHTML = "<p> Question: " + (currentQuestion + 1) + "/" + questionsPerQuiz + "<br>What letter does the sign represent?</p>";
}

function showCountdown()
{
    if(count <= maxTime)
    {
        countdown.innerHTML = "<p> Time left: " + (maxTime-count) + "</p>"; 
        count++;
    }
    else
    {
        clearInterval(timer);
        showScore();
    } 
}

function checkAnswer(answer)
{
    if(answer == questions[currentQuestion].correct)
    {
        score++;
    }

    if(currentQuestion < questionsPerQuiz - 1)
    {
        currentQuestion++;
        showQuestion();
    }
    else
    {
        clearInterval(timer);
        showScore();
    }
}

function showScore()
{
    scoreDiv.style.display = "block";
    quiz.style.display = "none";
    scoreDiv.innerHTML = "<p> You got "+ score + " out of " + questionsPerQuiz + " correct! </p>";
}


