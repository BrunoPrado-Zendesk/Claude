---
name: powerpoint-zendesk
description: Create, update, or review PowerPoint presentations with Zendesk branding. Use this skill whenever the user asks to create slides, make a presentation, update a deck, review slides, add charts or graphics to presentations, or work with presentation files. This includes requests like "create a sales deck", "update my presentation", "review these slides", "add charts to the deck", "make a presentation about X", or "generate slides for Y". Always use this skill for ANY presentation-related task, even if the user doesn't explicitly mention PowerPoint or slides - if they're talking about creating visual materials for a meeting, pitch, or demo, this skill applies.
compatibility:
  tools: [Read, Write, Bash, mcp__google-drive__gdrive_search, mcp__google-drive__gdrive_get_presentation]
---

# PowerPoint Presentation Skill with Zendesk Branding

Create, update, and review professional PowerPoint presentations following Zendesk Garden design system guidelines.

## Table of Contents

1. [When to Use This Skill](#when-to-use)
2. [Setup and Dependencies](#setup)
3. [Creating New Presentations](#creating-presentations)
4. [Updating Existing Presentations](#updating-presentations)
5. [Reviewing Presentations](#reviewing-presentations)
6. [Working with Google Drive](#google-drive)
7. [Chart and Graphics Generation](#charts)
8. [Zendesk Branding Guidelines](#branding)
9. [Common Presentation Types](#presentation-types)

## When to Use This Skill {#when-to-use}

Use this skill EVERY TIME the user mentions:
- Creating presentations, slides, or decks
- Updating or modifying existing presentations
- Reviewing presentation content or design
- Adding charts, graphics, or data visualizations
- Sales decks, product demos, executive briefings, case studies, business cases, ROI presentations
- Working with .pptx files or Google Slides
- Preparing materials for meetings, pitches, or demos

**Trigger phrases include:**
- "Create a presentation about..."
- "Make slides for..."
- "Update my deck"
- "Review this presentation"
- "Add charts showing..."
- "Generate a sales deck"
- "Build a demo presentation"
- "Create an executive briefing"

## Setup and Dependencies {#setup}

### Required Python Packages

```bash
pip install python-pptx matplotlib pillow google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### Available Scripts

The skill includes three helper scripts in the `scripts/` directory:
1. **`create_pptx.py`** - Main presentation builder with Zendesk branding
2. **`generate_charts.py`** - Chart generation with Zendesk colors
3. **`upload_to_drive.py`** - Google Drive integration helper

### Reference Documentation

- **`references/zendesk-brand.md`** - Complete Zendesk branding guidelines

## Creating New Presentations {#creating-presentations}

### Step-by-Step Process

1. **Understand Requirements**
   - Ask clarifying questions about:
     - Presentation topic and purpose
     - Target audience (sales prospects, executives, customers, internal team)
     - Presentation type (sales deck, product demo, case study, business case, ROI, executive briefing)
     - Key messages and content
     - Number of slides (typically 10-20)
     - Data or charts needed
     - Deadline and format preferences

2. **Plan the Structure**
   Based on presentation type, create an outline:
   - Title slide
   - Agenda/overview (optional for shorter decks)
   - Section dividers (for longer presentations)
   - Content slides
   - Data/chart slides
   - Case studies or examples
   - Closing/thank you slide

3. **Import and Initialize**
   ```python
   import sys
   sys.path.append('/path/to/skill/scripts')

   from create_pptx import (
       create_presentation,
       add_title_slide,
       add_content_slide,
       add_two_column_slide,
       add_section_header_slide,
       add_closing_slide,
       save_presentation,
       COLORS,
       FONT_SIZES
   )
   from generate_charts import (
       create_bar_chart,
       create_line_chart,
       create_pie_chart,
       create_horizontal_bar_chart,
       save_chart,
       fig_to_image
   )

   # Create presentation
   prs = create_presentation("Presentation Title")
   ```

4. **Build Slides**

   **Title Slide:**
   ```python
   add_title_slide(
       prs,
       "Main Title Here",
       "Subtitle or tagline"
   )
   ```

   **Content Slide with Bullets:**
   ```python
   add_content_slide(
       prs,
       "Slide Title",
       [
           "First bullet point",
           "Second bullet point",
           "Third bullet point",
           "Fourth bullet point"
       ]
   )
   ```

   **Two-Column Layout:**
   ```python
   add_two_column_slide(
       prs,
       "Comparison or Benefits",
       [
           "Left column point 1",
           "Left column point 2",
           "Left column point 3"
       ],
       [
           "Right column point 1",
           "Right column point 2",
           "Right column point 3"
       ]
   )
   ```

   **Section Header:**
   ```python
   add_section_header_slide(
       prs,
       "Section Name",
       "Optional subtitle"
   )
   ```

5. **Add Charts and Graphics**

   Generate charts as needed:
   ```python
   # Create chart
   chart_data = {
       'Q1': 125,
       'Q2': 185,
       'Q3': 210,
       'Q4': 245
   }
   fig = create_bar_chart(
       chart_data,
       "Quarterly Performance",
       "Revenue ($K)"
   )
   save_chart(fig, "chart.png")
   ```

   Add chart to slide:
   ```python
   from pptx.util import Inches

   # Create blank slide for chart
   slide_layout = prs.slide_layouts[6]
   slide = prs.slides.add_slide(slide_layout)

   # Add title
   from create_pptx import add_title_to_slide  # Helper if needed
   # Or manually add title text box

   # Add chart image
   slide.shapes.add_picture(
       "chart.png",
       Inches(1),
       Inches(2),
       width=Inches(11)
   )
   ```

6. **Add Closing Slide**
   ```python
   add_closing_slide(
       prs,
       "Thank You",
       [
           "Questions?",
           "contact@zendesk.com",
           "www.zendesk.com"
       ]
   )
   ```

7. **Save Presentation**
   ```python
   output_path = save_presentation(prs, "presentation_name.pptx")
   print(f"Presentation saved to: {output_path}")
   ```

### Content Guidelines

**For each slide:**
- **Title**: Clear, descriptive (max 60 characters)
- **Content**: 3-5 bullets maximum
- **Text**: Concise phrases, not full sentences
- **Visuals**: Prefer charts/images over text when possible
- **White space**: Don't overcrowd slides

**Content hierarchy:**
- Most important points first
- One main idea per slide
- Support with data/visuals
- Clear call-to-action on relevant slides

## Updating Existing Presentations {#updating-presentations}

### Workflow for Updates

1. **Retrieve Presentation**

   **Option A: From Google Drive**
   ```python
   # Search for presentation
   search_results = use_mcp_tool(
       'mcp__google-drive__gdrive_search',
       query="presentation_name type:presentation"
   )

   # Get presentation content
   presentation = use_mcp_tool(
       'mcp__google-drive__gdrive_get_presentation',
       presentation_id="<id_from_search>"
   )
   ```

   **Option B: From Local File**
   ```python
   from pptx import Presentation

   # Load existing presentation
   prs = Presentation("existing_presentation.pptx")
   ```

2. **Understand Required Changes**
   - What needs to be added?
   - What needs to be modified?
   - What needs to be removed?
   - Are there new charts or data to add?

3. **Make Modifications**

   **Add new slides:**
   ```python
   # Add new content slide
   add_content_slide(prs, "New Slide Title", ["Point 1", "Point 2"])
   ```

   **Modify existing slides:**
   ```python
   # Access specific slide
   slide = prs.slides[slide_index]

   # Modify text in shapes
   for shape in slide.shapes:
       if shape.has_text_frame:
           # Modify text
           shape.text_frame.text = "New text"
   ```

   **Delete slides:**
   ```python
   # Get slide ID
   slide_id = prs.slides[slide_index].slide_id

   # Remove slide
   rId = prs.slides._sldIdLst[slide_index].rId
   prs.part.drop_rel(rId)
   del prs.slides._sldIdLst[slide_index]
   ```

4. **Save Updated Presentation**
   ```python
   save_presentation(prs, "updated_presentation.pptx")
   ```

## Reviewing Presentations {#reviewing-presentations}

### Review Process

1. **Load Presentation**
   - From Google Drive or local file
   - Read content from all slides

2. **Review Criteria**

   **Content Quality:**
   - [ ] Clear messaging and structure
   - [ ] Appropriate amount of text (not too dense)
   - [ ] Logical flow between slides
   - [ ] Key points stand out
   - [ ] No typos or errors

   **Design Quality:**
   - [ ] Consistent Zendesk branding
   - [ ] Proper color usage
   - [ ] Appropriate font sizes
   - [ ] Good use of white space
   - [ ] Charts are clear and labeled

   **Accessibility:**
   - [ ] Sufficient color contrast
   - [ ] Text is readable
   - [ ] Not relying solely on color
   - [ ] Alt text for images (if applicable)

   **Technical:**
   - [ ] Slides numbered appropriately
   - [ ] File size reasonable (< 50MB)
   - [ ] Compatible format (.pptx)

3. **Provide Feedback**

   Structure feedback as:
   ```
   ## Presentation Review: [Title]

   ### Strengths
   - What works well
   - Effective elements

   ### Improvements Needed
   1. Specific issue with suggested fix
   2. Another issue with suggested fix

   ### Branding Compliance
   - Color usage: [Compliant/Needs adjustment]
   - Typography: [Compliant/Needs adjustment]
   - Layout: [Compliant/Needs adjustment]

   ### Recommendations
   - High-priority changes
   - Nice-to-have improvements
   ```

4. **Offer to Make Changes**
   - "Would you like me to implement these changes?"
   - Make revisions if user confirms

## Working with Google Drive {#google-drive}

### Accessing Presentations

**Search for presentations:**
```python
results = use_mcp_tool(
    'mcp__google-drive__gdrive_search',
    query="sales deck type:presentation"
)
```

**Get specific presentation:**
```python
presentation = use_mcp_tool(
    'mcp__google-drive__gdrive_get_presentation',
    presentation_id="<presentation-id>"
)
```

### Uploading to Google Drive

**Current Approach:**
1. Create .pptx file locally
2. Inform user where file is saved
3. Provide file path for manual upload OR
4. Offer to guide through upload process

**Note:** Direct .pptx upload to Google Drive via MCP requires additional API setup. For now, we create the file and user uploads manually or we provide clear instructions.

**Future:** When Google Drive write access is available, implement automatic upload.

## Chart and Graphics Generation {#charts}

### Chart Types Available

1. **Bar Chart** - Comparisons, categories
2. **Line Chart** - Trends over time
3. **Pie Chart** - Proportions, market share
4. **Horizontal Bar** - Rankings, comparisons
5. **Stacked Bar** - Component breakdowns

### Creating Charts

**Import chart functions:**
```python
from generate_charts import (
    create_bar_chart,
    create_line_chart,
    create_pie_chart,
    create_horizontal_bar_chart,
    create_stacked_bar_chart,
    save_chart
)
```

**Bar Chart Example:**
```python
data = {
    'Category A': 45,
    'Category B': 62,
    'Category C': 38,
    'Category D': 51
}
fig = create_bar_chart(
    data,
    title="Performance by Category",
    ylabel="Sales ($K)",
    color_scheme='primary'
)
save_chart(fig, "bar_chart.png")
```

**Line Chart Example:**
```python
trend_data = {
    'Metric 1': [100, 120, 145, 160, 190, 210],
    'Metric 2': [80, 95, 110, 125, 140, 155]
}
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
fig = create_line_chart(
    trend_data,
    months,
    title="Growth Trends",
    ylabel="Value",
    xlabel="Month"
)
save_chart(fig, "line_chart.png")
```

**Pie Chart Example:**
```python
distribution = {
    'Segment A': 35,
    'Segment B': 28,
    'Segment C': 22,
    'Segment D': 15
}
fig = create_pie_chart(
    distribution,
    title="Market Distribution"
)
save_chart(fig, "pie_chart.png")
```

### Chart Best Practices

- Use bar charts for comparisons
- Use line charts for trends
- Use pie charts sparingly (max 5-6 segments)
- Always label axes clearly
- Include data labels when helpful
- Choose appropriate color schemes
- Keep charts simple and focused

## Zendesk Branding Guidelines {#branding}

### Core Principles

**Always follow these Zendesk Garden guidelines:**

1. **Color Usage**
   - Primary: Blue #2694d6 for interactive elements and titles
   - Success: Green #26a178 for positive metrics
   - Warning: Yellow #d67305 for cautions
   - Danger: Red #eb5c69 for critical items
   - Text: Grey #5c6970 for body content

2. **Typography**
   - Titles: XXL or XXXL, Bold
   - Headings: XL, Bold
   - Body: MD, Regular
   - Captions: SM, Regular

3. **Accessibility**
   - Minimum 4.5:1 contrast for text
   - Minimum 3:1 contrast for graphics
   - Never use color alone - add text/icons

4. **White Space**
   - Don't overcrowd slides
   - Generous margins (0.5-0.75 inches)
   - Space between elements

### Brand Colors Reference

**Primary Colors (Hex):**
- Blue 600: #2694d6
- Blue 700: #1f73b7
- Grey 700: #5c6970
- Grey 300: #d8dcde
- Green 600: #26a178
- Red 600: #eb5c69
- Yellow 600: #d67305

**Secondary Colors:**
- Purple 600: #b276cd
- Teal 600: #2a9d8f
- Orange 600: #d57428
- Mint 600: #16a260

See `references/zendesk-brand.md` for complete color palette and guidelines.

## Common Presentation Types {#presentation-types}

### Sales Decks

**Structure:**
1. Title slide with hook
2. Problem statement
3. Solution overview
4. Key features/benefits
5. Customer success stories
6. ROI/value proposition
7. Pricing (if applicable)
8. Next steps/CTA
9. Thank you + contact

**Focus:** Customer value, ROI, social proof
**Colors:** Blue (primary), Green (success metrics)
**Charts:** Bar charts for comparisons, line charts for growth

### Product Demos

**Structure:**
1. Title slide
2. Product overview
3. Key features (one per slide with screenshots)
4. Use cases
5. Technical capabilities
6. Integration options
7. Demo video/screenshots
8. Q&A slide
9. Thank you + resources

**Focus:** Features, capabilities, ease of use
**Colors:** Blue (primary), Purple (innovation)
**Visuals:** Screenshots, product images, workflow diagrams

### Executive Briefings

**Structure:**
1. Title slide
2. Executive summary (key metrics)
3. Strategic objectives
4. Current status/progress
5. Key initiatives
6. Challenges and mitigation
7. Financial overview
8. Recommendations
9. Next steps
10. Thank you

**Focus:** High-level metrics, strategic direction
**Colors:** Blue (primary), Grey (professional)
**Charts:** KPI dashboards, trend lines

### Customer Case Studies

**Structure:**
1. Title slide with customer logo
2. Customer background
3. Challenge/problem
4. Solution implemented
5. Implementation process
6. Results/metrics (before/after)
7. Customer testimonial (quote)
8. Key takeaways
9. Thank you + contact

**Focus:** Customer success, measurable results
**Colors:** Green (success), Blue (trust)
**Visuals:** Customer logos, before/after charts, testimonial quotes

### Business Cases/ROI Presentations

**Structure:**
1. Title slide
2. Executive summary
3. Current situation/baseline
4. Proposed solution
5. Cost breakdown
6. Benefit analysis
7. ROI calculation
8. Implementation timeline
9. Risk assessment
10. Recommendation
11. Thank you

**Focus:** Financial analysis, ROI, timeline
**Colors:** Green (positive ROI), Teal (data), Blue (recommendations)
**Charts:** Financial projections, ROI curves, timelines

## Best Practices Summary

### Do:
✓ Use Zendesk brand colors consistently
✓ Keep slides focused and uncluttered
✓ Use charts to visualize data
✓ Include clear titles on every slide
✓ Maintain consistent formatting
✓ Test for accessibility (contrast)
✓ Number slides for easy reference
✓ Include sources for data/statistics

### Don't:
✗ Overcrowd slides with text
✗ Use colors that don't meet contrast requirements
✗ Mix too many fonts or styles
✗ Ignore white space
✗ Use generic stock photos without purpose
✗ Forget to proofread
✗ Make slides that can't stand alone

## Troubleshooting

**Issue: Python packages not found**
Solution: Install requirements: `pip install python-pptx matplotlib pillow`

**Issue: Charts not displaying correctly**
Solution: Check matplotlib backend, save to file first, then add to slide

**Issue: Google Drive access errors**
Solution: Verify MCP tools are configured, check permissions

**Issue: Fonts not displaying correctly**
Solution: Use system-safe fonts (Arial, Helvetica) or embed custom fonts

**Issue: File size too large**
Solution: Optimize images (< 5MB total), reduce image resolution

## Additional Resources

- **Zendesk Garden**: https://garden.zendesk.com
- **Brand Guidelines**: references/zendesk-brand.md (in this skill)
- **python-pptx Documentation**: https://python-pptx.readthedocs.io
- **Matplotlib Documentation**: https://matplotlib.org

## Support

For questions or issues with this skill:
1. Check the reference documentation
2. Review example code in scripts/
3. Consult Zendesk brand guidelines
4. Ask clarifying questions before proceeding

---

Remember: The goal is to create professional, branded presentations that effectively communicate the user's message. Always prioritize clarity, accessibility, and Zendesk brand compliance.
