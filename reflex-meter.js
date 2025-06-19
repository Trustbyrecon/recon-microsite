
document.addEventListener("DOMContentLoaded", function () {
    const score = 0.82;
    const scoreElement = document.getElementById("score");
    scoreElement.textContent = score.toFixed(2);

    let tier = "Novice";
    if (score >= 0.8) tier = "Echo";
    if (score >= 0.9) tier = "Anchor";
    if (score >= 0.95) tier = "Bloom";

    document.getElementById("tier").textContent = tier;
});
