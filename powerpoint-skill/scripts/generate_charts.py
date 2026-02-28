#!/usr/bin/env python3
"""
generate_charts.py - Chart generation with Zendesk branding

Creates charts and data visualizations using matplotlib with Zendesk Garden colors.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.figure import Figure
import numpy as np
from typing import List, Dict, Tuple, Optional
import io
from PIL import Image

# Zendesk Garden Color Palette (RGB normalized to 0-1)
COLORS = {
    'blue_600': (38/255, 148/255, 214/255),
    'blue_700': (31/255, 115/255, 183/255),
    'green_600': (38/255, 161/255, 120/255),
    'red_600': (235/255, 92/255, 105/255),
    'yellow_600': (214/255, 115/255, 5/255),
    'grey_700': (92/255, 105/255, 112/255),
    'purple_600': (178/255, 118/255, 205/255),
    'teal_600': (42/255, 157/255, 143/255),
    'orange_600': (213/255, 116/255, 40/255),
    'mint_600': (22/255, 162/255, 96/255),
}

# Color schemes for different chart types
COLOR_SCHEMES = {
    'primary': ['blue_600', 'green_600', 'purple_600', 'teal_600', 'orange_600'],
    'performance': ['green_600', 'blue_600', 'yellow_600', 'red_600'],
    'categories': ['blue_600', 'teal_600', 'purple_600', 'mint_600', 'orange_600'],
    'trend': ['blue_600', 'blue_700'],
}

def setup_chart_style():
    """Configure matplotlib to use Zendesk styling."""
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'DejaVu Sans']
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 11
    plt.rcParams['axes.titlesize'] = 13
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['legend.fontsize'] = 9
    plt.rcParams['figure.titlesize'] = 14

def create_bar_chart(
    data: Dict[str, float],
    title: str,
    ylabel: str = "Value",
    color_scheme: str = 'primary',
    figsize: Tuple[int, int] = (10, 6)
) -> Figure:
    """
    Create a bar chart with Zendesk branding.

    Args:
        data: Dictionary of labels and values
        title: Chart title
        ylabel: Y-axis label
        color_scheme: Color scheme to use
        figsize: Figure size (width, height)

    Returns:
        matplotlib Figure object
    """
    setup_chart_style()

    fig, ax = plt.subplots(figsize=figsize)

    labels = list(data.keys())
    values = list(data.values())

    # Get colors
    scheme_colors = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['primary'])
    colors = [COLORS[c] for c in scheme_colors[:len(labels)]]

    # Create bars
    bars = ax.bar(labels, values, color=colors, alpha=0.85)

    # Styling
    ax.set_title(title, fontweight='bold', pad=20)
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2.,
            height,
            f'{height:.1f}',
            ha='center',
            va='bottom',
            fontsize=9
        )

    plt.tight_layout()
    return fig

def create_line_chart(
    data: Dict[str, List[float]],
    x_labels: List[str],
    title: str,
    ylabel: str = "Value",
    xlabel: str = "",
    color_scheme: str = 'trend',
    figsize: Tuple[int, int] = (10, 6)
) -> Figure:
    """
    Create a line chart with Zendesk branding.

    Args:
        data: Dictionary of series names and their values
        x_labels: Labels for x-axis
        title: Chart title
        ylabel: Y-axis label
        xlabel: X-axis label
        color_scheme: Color scheme to use
        figsize: Figure size

    Returns:
        matplotlib Figure object
    """
    setup_chart_style()

    fig, ax = plt.subplots(figsize=figsize)

    # Get colors
    scheme_colors = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['trend'])
    colors = [COLORS[c] for c in scheme_colors]

    # Plot lines
    for i, (name, values) in enumerate(data.items()):
        color = colors[i % len(colors)]
        ax.plot(
            x_labels,
            values,
            marker='o',
            linewidth=2.5,
            markersize=6,
            color=color,
            label=name,
            alpha=0.9
        )

    # Styling
    ax.set_title(title, fontweight='bold', pad=20)
    ax.set_ylabel(ylabel, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel, fontweight='bold')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(alpha=0.3)
    ax.legend(frameon=False)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    return fig

def create_pie_chart(
    data: Dict[str, float],
    title: str,
    color_scheme: str = 'categories',
    figsize: Tuple[int, int] = (8, 8)
) -> Figure:
    """
    Create a pie chart with Zendesk branding.

    Args:
        data: Dictionary of labels and values
        title: Chart title
        color_scheme: Color scheme to use
        figsize: Figure size

    Returns:
        matplotlib Figure object
    """
    setup_chart_style()

    fig, ax = plt.subplots(figsize=figsize)

    labels = list(data.keys())
    values = list(data.values())

    # Get colors
    scheme_colors = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['categories'])
    colors = [COLORS[c] for c in scheme_colors[:len(labels)]]

    # Create pie chart
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        textprops={'fontsize': 10}
    )

    # Style percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')

    ax.set_title(title, fontweight='bold', pad=20)
    plt.tight_layout()
    return fig

def create_horizontal_bar_chart(
    data: Dict[str, float],
    title: str,
    xlabel: str = "Value",
    color_scheme: str = 'performance',
    figsize: Tuple[int, int] = (10, 6)
) -> Figure:
    """
    Create a horizontal bar chart (useful for rankings, comparisons).

    Args:
        data: Dictionary of labels and values
        title: Chart title
        xlabel: X-axis label
        color_scheme: Color scheme to use
        figsize: Figure size

    Returns:
        matplotlib Figure object
    """
    setup_chart_style()

    fig, ax = plt.subplots(figsize=figsize)

    labels = list(data.keys())
    values = list(data.values())

    # Get colors
    scheme_colors = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['performance'])
    colors = [COLORS[c] for c in scheme_colors[:len(labels)]]

    # Create horizontal bars
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, values, color=colors, alpha=0.85)

    # Styling
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()  # Labels read top-to-bottom
    ax.set_xlabel(xlabel, fontweight='bold')
    ax.set_title(title, fontweight='bold', pad=20)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='x', alpha=0.3)

    # Add value labels
    for i, (bar, value) in enumerate(zip(bars, values)):
        width = bar.get_width()
        ax.text(
            width,
            bar.get_y() + bar.get_height()/2,
            f' {value:.1f}',
            ha='left',
            va='center',
            fontsize=9
        )

    plt.tight_layout()
    return fig

def create_stacked_bar_chart(
    data: Dict[str, Dict[str, float]],
    title: str,
    ylabel: str = "Value",
    color_scheme: str = 'categories',
    figsize: Tuple[int, int] = (10, 6)
) -> Figure:
    """
    Create a stacked bar chart.

    Args:
        data: Nested dict: {category: {subcategory: value}}
        title: Chart title
        ylabel: Y-axis label
        color_scheme: Color scheme to use
        figsize: Figure size

    Returns:
        matplotlib Figure object
    """
    setup_chart_style()

    fig, ax = plt.subplots(figsize=figsize)

    categories = list(data.keys())
    subcategories = list(next(iter(data.values())).keys())

    # Get colors
    scheme_colors = COLOR_SCHEMES.get(color_scheme, COLOR_SCHEMES['categories'])
    colors = [COLORS[c] for c in scheme_colors[:len(subcategories)]]

    # Prepare data
    x = np.arange(len(categories))
    width = 0.6
    bottom = np.zeros(len(categories))

    # Create stacked bars
    for i, subcat in enumerate(subcategories):
        values = [data[cat][subcat] for cat in categories]
        ax.bar(
            x,
            values,
            width,
            label=subcat,
            bottom=bottom,
            color=colors[i],
            alpha=0.85
        )
        bottom += values

    # Styling
    ax.set_title(title, fontweight='bold', pad=20)
    ax.set_ylabel(ylabel, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend(frameon=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    return fig

def save_chart(fig: Figure, filename: str, dpi: int = 150) -> str:
    """
    Save chart to file.

    Args:
        fig: matplotlib Figure object
        filename: Output filename (png, jpg, or svg)
        dpi: Resolution for raster formats

    Returns:
        Full path to saved file
    """
    fig.savefig(filename, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return filename

def fig_to_image(fig: Figure, dpi: int = 150) -> Image:
    """
    Convert matplotlib figure to PIL Image.

    Args:
        fig: matplotlib Figure object
        dpi: Resolution

    Returns:
        PIL Image object
    """
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=dpi, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    img = Image.open(buf)
    plt.close(fig)
    return img

# Example usage
if __name__ == "__main__":
    # Bar chart example
    sales_data = {
        'Q1': 125,
        'Q2': 185,
        'Q3': 210,
        'Q4': 245
    }
    fig1 = create_bar_chart(
        sales_data,
        "Quarterly Sales Performance",
        "Revenue ($ thousands)"
    )
    save_chart(fig1, "sales_bar_chart.png")

    # Line chart example
    trend_data = {
        'Product A': [100, 120, 145, 160, 190],
        'Product B': [80, 95, 110, 125, 140]
    }
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    fig2 = create_line_chart(
        trend_data,
        months,
        "Product Performance Trends",
        "Units Sold",
        "Month"
    )
    save_chart(fig2, "trend_line_chart.png")

    # Pie chart example
    market_share = {
        'Segment A': 35,
        'Segment B': 28,
        'Segment C': 22,
        'Segment D': 15
    }
    fig3 = create_pie_chart(
        market_share,
        "Market Share Distribution"
    )
    save_chart(fig3, "market_pie_chart.png")

    print("Sample charts created successfully!")
