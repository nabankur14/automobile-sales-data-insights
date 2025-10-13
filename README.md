<h1 align="center" style="color:#2b7a78;">Automobile Customer Analytics</h1>
<h3 align="center" style="color:#17252a;">Data-Driven Insights for Austro Motor Company (AMC)</h3>

<p align="center">
  <strong>Author:</strong> <a href="https://github.com/nabankur14" target="_blank" style="color:#3aafa9;">Nabankur Ray</a>  
</p>

<hr>

<h2 style="color:#17252a;">Overview</h2>
<p>
This project focuses on <strong>Automobile Customer Analytics</strong> — analyzing customer purchasing behavior using demographic, financial, and vehicle data for <strong>Austro Motor Company (AMC)</strong>.  
By leveraging <em>data analytics</em> and <em>visualization techniques</em>, it identifies high-potential customer segments, uncovers car type preferences, and provides <strong>actionable business insights</strong> for targeted marketing and sales optimization.
</p>

<details open>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Objective</summary>
  <p>
  The goal of this analysis is to:
  <ul>
    <li>Understand how <strong>demographic and financial factors</strong> influence car purchase decisions.</li>
    <li>Identify key <strong>customer segments</strong> (gender, marital status, income group) for better marketing campaigns.</li>
    <li>Analyze patterns across <strong>car types (SUV, Sedan, Hatchback)</strong> and spending behavior.</li>
    <li>Provide <strong>data-backed business recommendations</strong> for improved targeting and customer satisfaction.</li>
  </ul>
  </p>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Dataset</summary>
  <ul>
    <li><strong>Source:</strong> Austro Automobile (AMC) Customer Dataset – <code>austo_automobile.csv</code></li>
    <li><strong>Size:</strong> 1,581 rows × 14 columns</li>
    <li><strong>Key Features:</strong>
      <ul>
        <li>Demographics: Gender, Age, Marital Status, Education, Dependents</li>
        <li>Financials: Salary, Partner Salary, Total Salary, Personal Loan, Housing Loan, Partner Working</li>
        <li>Vehicle Info: Car Type (SUV, Sedan, Hatchback), Price</li>
      </ul>
    </li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Methodology</summary>
  <ol>
    <li><strong>Data Cleaning & Preprocessing:</strong> Handled missing values, corrected categorical entries (e.g., “Femal” → “Female”), derived missing partner salaries using logical imputation.</li>
    <li><strong>Exploratory Data Analysis (EDA):</strong> Visualized distributions, correlations, and segment trends using bar charts, boxplots, and pair plots.</li>
    <li><strong>Feature Analysis:</strong> Compared spending patterns and car preferences across gender, profession, and marital status.</li>
    <li><strong>Statistical Insights:</strong> Quantified mean car prices, correlations between salary, dependents, and purchase type.</li>
    <li><strong>Business Interpretation:</strong> Converted analytical findings into actionable marketing and sales recommendations.</li>
  </ol>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Tools & Technologies</summary>
  <p>
  <code>Python</code>, <code>Pandas</code>, <code>NumPy</code>, <code>Matplotlib</code>, <code>Seaborn</code>,  
  <code>Jupyter Notebook</code>, <code>Microsoft Excel</code>, <code>Statistical Analysis</code>
  </p>
</details>

<details open>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Results & Insights</summary>
  <p>
  <strong>Key Analytical Findings:</strong>
  <ul>
    <li><strong>Gender Trends:</strong> Female customers spend more on cars (avg. $47,705) than male customers (avg. $32,817).</li>
    <li><strong>Profession Insights:</strong> Salaried individuals dominate car purchases (especially Sedans).</li>
    <li><strong>Car Type Popularity:</strong> Sedans are the most purchased cars; SUVs are least preferred.</li>
    <li><strong>Financial Behavior:</strong> Personal loans have minimal influence on car purchase price.</li>
    <li><strong>Household Dynamics:</strong> Having a working partner slightly lowers average car spending.</li>
  </ul>
  <p>
  <strong>Actionable Insights:</strong>
  Target <strong>married, salaried individuals without housing loans</strong> — the most promising customer group for high-value car sales.  
  Leverage gender-based marketing to attract female customers who prefer premium-priced vehicles.  
  </p>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Future Scope</summary>
  <ul>
    <li>Integrate <strong>predictive models</strong> to forecast car purchase likelihood.</li>
    <li>Develop an <strong>interactive Power BI dashboard</strong> for real-time insights.</li>
    <li>Include <strong>geographical and behavioral data</strong> for deeper segmentation.</li>
    <li>Automate reports for ongoing sales performance tracking.</li>
  </ul>
</details>

<details>
  <summary style="cursor:pointer; color:#3aafa9; font-weight:bold;">Folder Structure</summary>
  <pre style="background:#f0f0f0; padding:10px; border-radius:8px;">
Austo_Automobile.ipynb       → Jupyter notebooks for data cleaning and EDA
austo_automobile.csv            → Raw and processed customer datasets
Automobile_Sales_Data_Insights.pdf → Full business & technical report
README.md        → Project documentation (this file)
  </pre>
</details>

<hr>
<p align="center" style="font-size:14px; color:#555;">
© 2025 <strong>Nabankur Ray</strong> | Data Scientist 
</p> 
