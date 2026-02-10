function attachCopyButtons() {
    document.querySelectorAll("[data-copy]").forEach((button) => {
        button.addEventListener("click", async () => {
            const targetId = button.getAttribute("data-copy");
            const block = document.getElementById(targetId);
            if (!block) {
                return;
            }
            try {
                await navigator.clipboard.writeText(block.innerText.trim());
                const previous = button.textContent;
                button.textContent = "Скопировано!";
                button.disabled = true;
                setTimeout(() => {
                    button.textContent = previous;
                    button.disabled = false;
                }, 1200);
            } catch (error) {
                alert("Не удалось скопировать код. Скопируйте вручную.");
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", attachCopyButtons);
