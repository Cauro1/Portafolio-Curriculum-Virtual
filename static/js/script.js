// Funcionalidades básicas para el portafolio
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling para enlaces de navegación
    const navLinks = document.querySelectorAll('.nav-links a');
    
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop - 80;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Efecto de navbar al hacer scroll
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.style.background = 'var(--bg-white)';
            navbar.style.backdropFilter = 'none';
        }
    });

    // Manejo del formulario de contacto
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitButton = this.querySelector('button[type="submit"]');
            const originalText = submitButton.textContent;
            
            // Mostrar estado de carga
            submitButton.textContent = 'Enviando...';
            submitButton.disabled = true;
            
            try {
                const response = await fetch('/contact', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    alert('¡Mensaje enviado con éxito! Te contactaré pronto.');
                    contactForm.reset();
                } else {
                    throw new Error(result.message || 'Error al enviar el mensaje');
                }
            } catch (error) {
                console.error('Error:', error);
                alert('Error al enviar el mensaje. Por favor, inténtalo de nuevo.');
            } finally {
                // Restaurar botón
                submitButton.textContent = originalText;
                submitButton.disabled = false;
            }
        });
    }

    // Efectos de hover para tarjetas de proyecto
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    console.log('Portafolio cargado correctamente');
});