"""
SVG Project Card Generator for GitHub README
Creates Bootstrap-style animated cards with project details
"""

import os
import re


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_svg_icon_content(tech_name):
    """
    Load and extract SVG content from tech icon file.
    
    Args:
        tech_name: Name of the technology
        
    Returns:
        str: Inner SVG content without the outer <svg> tag, or None if not found
    """
    # Map tech names to icon filenames
    icon_mapping = {
        '.NET8': 'dotnet8.svg',
        '.NET': 'dotnetcore.svg',
        'React': 'react.svg',
        'TypeScript': 'typescript.svg',
        'Azure': 'azure.svg',
        'Azure AI': 'azure.svg',
        'Docker': 'docker.svg',
        'Angular': 'angular.svg',
        'SQL Server': 'sqlserver.svg',
        'Redis': 'redis.svg',
        'Stripe': 'stripe.svg',
        'Azure Functions': 'azure-functions.svg',
        'RabbitMQ': 'rabbitmq.svg',
        'PostgreSQL': 'postgresql.svg',
        'IdentityServer': 'dotnetcore.svg',
        'JWT': 'jwt.svg',
        'CQRS': 'cqrs.svg',
        'MediatR': 'mediatr.svg',
        'Fluent Validation': 'fluentvalidation.svg',
        'EF Core': 'dotnetcore.svg',
        'Kubernetes': 'kubernetes.svg',
        'Consul': 'consul.svg',
        'Ocelot': 'dotnetcore.svg',
        'OpenAI API': 'openai.svg',
        'ML.NET': 'mlnet.svg',
        'LangChain': 'dotnetcore.svg',
        'ONNX': 'onnx.svg',
        'TensorFlow': 'tensorflow.svg',
    }
    
    icon_filename = icon_mapping.get(tech_name)
    if not icon_filename:
        return None
    
    icon_path = f"assets/icons/tech/{icon_filename}"
    if not os.path.exists(icon_path):
        return None
    
    try:
        with open(icon_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Extract content between <svg> tags
        match = re.search(r'<svg[^>]*>(.*?)</svg>', svg_content, re.DOTALL)
        if match:
            return match.group(1).strip()
        return None
    except Exception as e:
        print(f"⚠️  Could not load icon for {tech_name}: {e}")
        return None


def get_tech_color(tech):
    """
    Return the brand color for a specific technology.
    
    Args:
        tech: Technology name
        
    Returns:
        str: Hex color code
    """
    colors = {
        '.NET 8': '#512BD4',
        '.NET': '#512BD4',
        'React': '#61DAFB',
        'TypeScript': '#007ACC',
        'Azure': '#0078D4',
        'Docker': '#2496ED',
        'Angular': '#DD0031',
        'SQL Server': '#CC2927',
        'Redis': '#DC382D',
        'Stripe': '#008CDD',
        'Azure Functions': '#0078D4',
        'RabbitMQ': '#FF6600',
        'PostgreSQL': '#336791',
        'IdentityServer': '#512BD4',
        'JWT': '#000000',
        'CQRS': '#512BD4',
        'MediatR': '#512BD4',
        'FluentValidation': '#512BD4',
        'EF Core': '#512BD4',
        'Kubernetes': '#326CE5',
        'Consul': '#F24C53',
        'Ocelot': '#512BD4',
        'OpenAI API': '#10A37F',
        'ML.NET': '#512BD4',
        'LangChain': '#1C3C3C',
        'ONNX': '#005CED',
        'TensorFlow': '#FF6F00',
    }
    return colors.get(tech, '#f75c03')


def adjust_color(hex_color, percent):
    """
    Lighten or darken a hex color by a percentage.
    
    Args:
        hex_color: Hex color code
        percent: Percentage to adjust
        
    Returns:
        str: Adjusted hex color code
    """
    # Simple implementation - returns the same color
    # Can be extended for actual color manipulation
    return hex_color


# ============================================================================
# MAIN CARD GENERATION FUNCTION
# ============================================================================

def generate_project_card(
    title,
    emoji,
    description_line1,
    tech_stack,
    links,
    stats,
    output_filename,
    theme_color="#f75c03"
):
    """
    Generate an animated SVG card for a project
    
    Args:
        title: Project title
        emoji: Emoji icon for the project
        description_line1: First line of description
        tech_stack: List of technologies (max 5-6)
        links: Dict with keys: readme, demo, docs, repo
        stats: Dict with keys: stars, issues, updated
        output_filename: Name of the output SVG file
        theme_color: Primary color for the theme
    """
    
    # Calculate tech icon-box positions (70px wide boxes)
    tech_badges = []
    x_position = 20
    box_width = 70
    box_height = 60
    spacing = 15  # Gap between boxes

    for i, tech in enumerate(tech_stack[:5]):  # Limit to 5 tech items for icon-box layout
        icon_content = get_svg_icon_content(tech)
        tech_badges.append({
            'text': tech,
            'x': x_position,
            'width': box_width,
            'height': box_height,
            'color': get_tech_color(tech),
            'icon': icon_content
        })
        x_position += box_width + spacing
    
    # Create unique gradient IDs for this card
    gradient_id = output_filename.replace('.svg', '')
    
    svg_content = f'''<svg width="500" height="320" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- 3D Radial gradient for depth (center glow) -->
    <radialGradient id="radialDepth_{gradient_id}" cx="50%" cy="50%" r="70%">
      <stop offset="0%" style="stop-color:#1e2838;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#171b28;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0a0d15;stop-opacity:1" />
    </radialGradient>
    
    <!-- Diagonal gradient overlay for 3D effect -->
    <linearGradient id="diagonalGradient_{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0f1520;stop-opacity:1" />
      <stop offset="20%" style="stop-color:#1a2030;stop-opacity:0.9" />
      <stop offset="40%" style="stop-color:#212a3d;stop-opacity:0.7" />
      <stop offset="60%" style="stop-color:#1a2030;stop-opacity:0.9" />
      <stop offset="100%" style="stop-color:#0a0d15;stop-opacity:1" />
    </linearGradient>
    
    <!-- 3D Light reflection from top-left -->
    <linearGradient id="lightReflection_{gradient_id}" x1="0%" y1="0%" x2="50%" y2="50%">
      <stop offset="0%" style="stop-color:{theme_color};stop-opacity:0.4" />
      <stop offset="50%" style="stop-color:{theme_color};stop-opacity:0.1" />
      <stop offset="100%" style="stop-color:{theme_color};stop-opacity:0" />
    </linearGradient>
    
    <!-- Bottom shadow for depth -->
    <linearGradient id="bottomShadow_{gradient_id}" x1="0%" y1="80%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#000000;stop-opacity:0" />
      <stop offset="100%" style="stop-color:#000000;stop-opacity:0.6" />
    </linearGradient>
    
    <!-- Header gradient with 3D effect -->
    <linearGradient id="headerGradient_{gradient_id}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:{theme_color};stop-opacity:0.7" />
      <stop offset="50%" style="stop-color:{theme_color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{theme_color};stop-opacity:0.7" />
    </linearGradient>
    
    <!-- Accent glow gradient -->
    <radialGradient id="accentGlow_{gradient_id}" cx="50%" cy="30%" r="60%">
      <stop offset="0%" style="stop-color:{theme_color};stop-opacity:0.3" />
      <stop offset="50%" style="stop-color:{theme_color};stop-opacity:0.15" />
      <stop offset="100%" style="stop-color:{theme_color};stop-opacity:0" />
    </radialGradient>
    
    <!-- Icon circle gradient (purple to theme color) -->
    <linearGradient id="iconCircleGradient_{gradient_id}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#512BD4;stop-opacity:1" />
      <stop offset="100%" style="stop-color:{theme_color};stop-opacity:1" />
    </linearGradient>
    
    <style>
      .card-bg {{
        stroke: {theme_color};
        stroke-width: 2;
      }}
      .card-bg:hover {{
        stroke: {theme_color};
        stroke-width: 3;
        filter: drop-shadow(0 0 20px {theme_color}60);
      }}
      .card-header {{
        fill: url(#headerGradient_{gradient_id});
      }}
      .title {{
        fill: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 22px;
        font-weight: bold;
      }}
      .emoji {{
        font-size: 24px;
      }}
      .description {{
        fill: #b8b9c5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 13px;
      }}
      .tech-label {{
        fill: {theme_color};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 12px;
        font-weight: bold;
      }}
      .tech-badge {{
        fill: #2a2b37;
        stroke: {theme_color};
        stroke-width: 1;
      }}
      .tech-text {{
        fill: #ffffff;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 11px;
      }}
      .link-text {{
        fill: #b8b9c5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 11px;
        cursor: pointer;
      }}
      .link-text:hover {{
        fill: {theme_color};
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
      }}
      @keyframes slideIn {{
        from {{ transform: translateX(-20px); opacity: 0; }}
        to {{ transform: translateX(0); opacity: 1; }}
      }}
      .animate-fade {{
        animation: fadeIn 0.6s ease-out;
      }}
      .animate-slide {{
        animation: slideIn 0.8s ease-out;
      }}
      .animate-pulse {{
        animation: pulse 2s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Main card background with 3D layered effect -->
  <rect width="500" height="320" fill="url(#radialDepth_{gradient_id})" rx="12"/>
  <rect width="500" height="320" fill="url(#diagonalGradient_{gradient_id})" rx="12"/>
  <rect width="500" height="320" fill="url(#lightReflection_{gradient_id})" rx="12"/>
  <rect width="500" height="320" fill="url(#accentGlow_{gradient_id})" rx="12"/>
  <rect width="500" height="320" fill="url(#bottomShadow_{gradient_id})" rx="12"/>
  
  <!-- Border -->
  <rect width="500" height="320" fill="none" stroke="{theme_color}" stroke-width="2" rx="12"/>
  
  <!-- Header Section with 3D edge highlights -->
  <rect x="0" y="0" width="500" height="50" fill="url(#headerGradient_{gradient_id})" rx="12"/>
  <line x1="0" y1="49" x2="500" y2="49" stroke="{theme_color}" stroke-width="1.5" opacity="0.7"/>
  <line x1="0" y1="50" x2="500" y2="50" stroke="#000000" stroke-width="1" opacity="0.5"/>
  
  <!-- Title with Emoji in Gradient Circle -->
  <circle cx="33" cy="30" r="18" fill="url(#iconCircleGradient_{gradient_id})" opacity="0.9"/>
  <text x="33" y="30" font-size="20" text-anchor="middle" dominant-baseline="middle">{emoji}</text>
  <text x="60" y="35" font-size="18" font-weight="bold" fill="#E0E0E0" class="card-title">{title}</text>
  
  <!-- Description -->
  <text class="description animate-fade" x="20" y="80">{description_line1}</text>
  
  <!-- Tech Stack Label -->
  <text class="tech-label" x="20" y="120">🔧 Tech Stack:</text>
  
  <!-- Tech Icons - Icon Boxes -->
  <g class="animate-slide">
'''
    
    # Add tech icon-boxes with SVG icons and labels
    for i, badge in enumerate(tech_badges):
        box_x = badge['x']
        box_y = 135
        circle_radius = 30  # Radius for circular icon-box
        circle_cx = box_x + 35  # Center X (70/2)
        circle_cy = box_y + 30  # Center Y (radius + offset)
        
        # Adjust scale based on tech name for better fit
        tech_name = badge['text']
        if tech_name in ['ML.NET', 'ONNX', 'OpenAI']:
            icon_scale = 0.50  # Larger scale for smaller detailed logos
        else:
            icon_scale = 0.35  # Default scale for most icons
            
        icon_x = circle_cx  # Center icon at circle center
        icon_y = circle_cy  # Center icon at circle center
        label_y = box_y + circle_radius * 2 + 15  # Label position below the circle
        label_x = circle_cx  # Center label
        
        # Check if tech name has multiple words for two-line label
        tech_words = badge['text'].split()
        is_two_words = len(tech_words) == 2
        
        svg_content += f'''    <!-- {badge['text']} Icon Box -->
    <g>
      <title>{badge['text']}</title>
      <circle class="tech-badge" cx="{circle_cx}" cy="{circle_cy}" r="{circle_radius}" fill="#1a1b27" stroke="{theme_color}" stroke-width="1.5" opacity="0.8"/>
      <g transform="translate({icon_x}, {icon_y}) scale({icon_scale})">
        <g transform="translate(-64, -64)">
          {badge['icon']}
        </g>
      </g>
'''
        
        # Add label below the circle (split into two lines if two words, otherwise single line)
        if is_two_words:
            svg_content += f'''      <text class="tech-text" x="{label_x}" y="{label_y}" text-anchor="middle" font-size="8" fill="{theme_color}" font-weight="bold">{tech_words[0]}</text>
      <text class="tech-text" x="{label_x}" y="{label_y + 9}" text-anchor="middle" font-size="8" fill="{theme_color}" font-weight="bold">{tech_words[1]}</text>
'''
        else:
            svg_content += f'''      <text class="tech-text" x="{label_x}" y="{label_y}" text-anchor="middle" font-size="8" fill="{theme_color}" font-weight="bold">{badge['text']}</text>
'''
        
        svg_content += '''    </g>
'''
    
    svg_content += '''  </g>
'''
    
    # Add links section
    svg_content += f'''
  <!-- Links Section -->
  <!-- <text class="tech-label" x="20" y="230">🔗 Links:</text> -->
  
  <!-- README Link -->
  <a href="{links.get('readme', '#')}" target="_blank">
    <text class="link-text" x="20" y="250">📖 README</text>
  </a>
  
  <!-- Quick Start Link -->
  <a href="{links.get('quickstart', links.get('demo', '#'))}" target="_blank">
    <text class="link-text" x="120" y="250">🚀 Quick Start</text>
  </a>
  
  <!-- Docs Link -->
  <a href="{links.get('docs', '#')}" target="_blank">
    <text class="link-text" x="230" y="250">📘 Docs</text>
  </a>
  
  <!-- Download Link -->
  <a href="{links.get('download', links.get('repo', '#'))}" target="_blank">
    <text class="link-text" x="310" y="250">📥 Download</text>
  </a>
  
  <!-- Stats Section -->
  <!-- <text class="tech-label" x="20" y="280">📊 Stats:</text> -->
  
  <!-- Stats Badges - Impact Focus -->
  <!-- <rect class="tech-badge" x="20" y="260" width="80" height="20" rx="3"/> -->
  <text class="tech-text" x="20" y="290">⭐ {stats.get('stars', '0')} Stars</text>
  
  <!-- <rect class="tech-badge" x="110" y="260" width="80" height="20" rx="3"/> -->
  <text class="tech-text" x="110" y="290">🍴 {stats.get('forks', '0')} Forks</text>
  
  <!-- <rect class="tech-badge" x="200" y="260" width="100" height="20" rx="3"/> -->
  <text class="tech-text" x="190" y="290">📦 {stats.get('downloads', '0')} Downloads</text>

  <!-- <rect class="tech-badge" x="310" y="260" width="90" height="20" rx="3"/> -->
  <text class="tech-text" x="310" y="290">✅ {stats.get('build', 'Passing')}</text>
  
  <!-- <rect class="tech-badge" x="310" y="260" width="90" height="20" rx="3"/> -->
  <text class="tech-text" x="380" y="290">🧪 {stats.get('coverage', '0')} Coverage</text>

  <!-- Decorative Pulse Elements -->
  <circle class="animate-pulse" cx="470" cy="30" r="8" fill="{theme_color}" opacity="0.3"/>
  <circle class="animate-pulse" cx="455" cy="30" r="5" fill="{theme_color}" opacity="0.2" style="animation-delay: 0.5s"/>
  <circle class="animate-pulse" cx="485" cy="30" r="4" fill="{theme_color}" opacity="0.15" style="animation-delay: 1s"/>
</svg>'''
    
    # Write to file
    with open(f"assets/images/project-cards/{output_filename}", "w", encoding="utf-8") as f:
        f.write(svg_content)
    
    print(f"✅ Created: {output_filename}")


# ============================================================================
# PROJECT CONFIGURATIONS
# ============================================================================

# Generate all project cards
if __name__ == "__main__":
    
    # Project 1: DistributedQueue.Kafka
    generate_project_card(
        title="DistributedQueue.Kafka",
        emoji="📱",
        description_line1="A modular, in-memory and Confluent Cloud Kafka distributed queue system, built with C# and .NET 9.0.",
        tech_stack=[".NET8", "React", "TypeScript", "Azure", "Docker"],
        links={
            "readme": "https://github.com/awalekeeran/DistributedQueue.Kafka#readme",
            "quickstart": "https://github.com/awalekeeran/DistributedQueue.Kafka/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/DistributedQueue.Kafka/wiki",
            "download": "https://github.com/awalekeeran/DistributedQueue.Kafka/releases/latest"
        },
        stats={"stars": "124", "forks": "28", "downloads": "2.3K", "build": "Passing", "coverage": "92%"},
        output_filename="devcontenthub.svg"
    )
    
    # Project 2: E-Commerce Platform
    generate_project_card(
        title="E-Commerce Platform",
        emoji="🛒",
        description_line1="Full-featured e-commerce solution with payment integration and scalability.",
        tech_stack=[".NET8", "Angular", "SQL Server", "Redis", "Stripe"],
        links={
            "readme": "https://github.com/awalekeeran/ECommercePlatform#readme",
            "quickstart": "https://github.com/awalekeeran/ECommercePlatform/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/ECommercePlatform/wiki",
            "download": "https://github.com/awalekeeran/ECommercePlatform/releases/latest"
        },
        stats={"stars": "198", "forks": "45", "downloads": "5.1K", "build": "Passing", "coverage": "85%"},
        output_filename="ecommerce.svg",
        theme_color="#00C853"
    )
    
    # Project 3: Notification System
    generate_project_card(
        title="Notification System",
        emoji="🔐",
        description_line1="Enterprise-grade notification service with multi-channel support.",
        tech_stack=[".NET8", "Azure Functions", "RabbitMQ", "Redis"],
        links={
            "readme": "https://github.com/awalekeeran/NotificationSystem#readme",
            "quickstart": "https://github.com/awalekeeran/NotificationSystem/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/NotificationSystem/wiki",
            "download": "https://github.com/awalekeeran/NotificationSystem/releases/latest"
        },
        stats={"stars": "86", "forks": "19", "downloads": "1.4K", "build": "Passing", "coverage": "90%"},
        output_filename="notification.svg",
        theme_color="#7C4DFF"
    )
    
    # Project 4: Authentication Service
    generate_project_card(
        title="Authentication Service",
        emoji="🔑", 
        description_line1="OAuth 2.0 / OpenID Connect authentication service.",
        tech_stack=[".NET8", "IdentityServer", "JWT", "Redis"],
        links={
            "readme": "https://github.com/awalekeeran/AuthenticationService#readme",
            "quickstart": "https://github.com/awalekeeran/AuthenticationService/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/AuthenticationService/wiki",
            "download": "https://github.com/awalekeeran/AuthenticationService/releases/latest"
        },
        stats={"stars": "142", "forks": "33", "downloads": "3.2K", "build": "Passing", "coverage": "85%"},
        output_filename="authentication.svg",
        theme_color="#FF5722"
    )
    
    # Project 5: CleanArchitectureTemplate
    generate_project_card(
        title="Clean Architecture Template",
        emoji="🏗️",
        description_line1="Production-ready .NET template with best practices and clean architecture.",
        tech_stack=[".NET8", "CQRS", "MediatR", "Fluent Validation"],
        links={
            "readme": "https://github.com/awalekeeran/CleanArchitectureTemplate#readme",
            "quickstart": "https://github.com/awalekeeran/CleanArchitectureTemplate/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/CleanArchitectureTemplate/wiki",
            "download": "https://github.com/awalekeeran/CleanArchitectureTemplate/releases/latest"
        },
        stats={"stars": "247", "forks": "52", "downloads": "1.2K", "build": "Passing", "coverage": "85%"},
        output_filename="cleanarch.svg",
        theme_color="#00BCD4"
    )
    
    # Project 6: Micro-services Starter
    generate_project_card(
        title="Micro-services Starter",
        emoji="🔄",
        description_line1="Microservices starter kit with service discovery and API gateway.",
        tech_stack=[".NET8", "Docker", "Kubernetes", "Consul"],
        links={
            "readme": "https://github.com/awalekeeran/MicroservicesStarter#readme",
            "quickstart": "https://github.com/awalekeeran/MicroservicesStarter/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/MicroservicesStarter/wiki",
            "download": "https://github.com/awalekeeran/MicroservicesStarter/releases/latest"
        },
        stats={"stars": "176", "forks": "41", "downloads": "4.7K", "build": "Passing", "coverage": "90%"},
        output_filename="microservices.svg",
        theme_color="#9C27B0"
    )
    
    # Project 7: AI-DotNet-Integration
    generate_project_card(
        title="AI-DotNet-Integration",
        emoji="🧠",
        description_line1="AI service integration examples for .NET developers.",
        tech_stack=[".NET8", "OpenAI API", "Azure AI", "ML.NET"],
        links={
            "readme": "https://github.com/awalekeeran/AI-DotNet-Integration#readme",
            "quickstart": "https://github.com/awalekeeran/AI-DotNet-Integration/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/AI-DotNet-Integration/wiki",
            "download": "https://github.com/awalekeeran/AI-DotNet-Integration/releases/latest"
        },
        stats={"stars": "312", "forks": "67", "downloads": "8.9K", "build": "Passing", "coverage": "85%"},
        output_filename="ai-integration.svg",
        theme_color="#10A37F"
    )
    
    # Project 8: MLNetExamples
    generate_project_card(
        title="ML.Net Examples",
        emoji="📊",
        description_line1="Machine learning examples using ML.NET framework.",
        tech_stack=[".NET8", "ML.NET", "ONNX", "TensorFlow"],
        links={
            "readme": "https://github.com/awalekeeran/MLNetExamples#readme",
            "quickstart": "https://github.com/awalekeeran/MLNetExamples/wiki/Quick-Start",
            "docs": "https://github.com/awalekeeran/MLNetExamples/wiki",
            "download": "https://github.com/awalekeeran/MLNetExamples/releases/latest"
        },
        stats={"stars": "203", "forks": "48", "downloads": "6.4K", "build": "Passing", "coverage": "90%"},
        output_filename="mlnet.svg",
        theme_color="#FF6F00"
    )
    
    print("\n✨ All project cards generated successfully!")
    print("📁 Location: assets/images/project-cards/")
    print("\n🎨 Card Features:")
    print("  ✅ Bootstrap-style card design")
    print("  ✅ Fade-in and slide-in animations")
    print("  ✅ Hover effects (glow and scale)")
    print("  ✅ Pulsing decorative elements")
    print("  ✅ Tech stack with colored icons")
    print("  ✅ Clickable links to repo/docs")
    print("  ✅ Project stats display")
    print("  ✅ Color-coded by category")
