"""
WHOLE FOODS MARKET — PRICE IMAGE RESET (EXACT ILLUSTRATED UI LAUNCHER FOR VS CODE)
HAVK Web Development Competition | Pulkit Tomar (UNC Charlotte)

HOW TO RUN IN VS CODE:
Click the 'Run Python File' (▶) button in the top-right corner of VS Code!
It will automatically generate `index.html` (with all custom SVG product images,
sharp 90-degree Swiss grids, and live thermal receipt) and open it in your browser.
"""

import os
import webbrowser
import http.server
import socketserver
import threading

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Whole Foods Market — Price Image Reset | HAVK Web Dev Competition</title>
  <!-- Google Fonts: Fraunces (Display Serif), Plus Jakarta Sans (Clean UI), JetBrains Mono (Audit Data) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700;9..144,800&family=JetBrains+Mono:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            wf: {
              emerald: '#004E36',
              emeraldDark: '#003826',
              emeraldLight: '#E6F0EC',
              alabaster: '#F4F1EA',
              paper: '#FFFDF9',
              ink: '#111111',
              saffron: '#E5A000',
              saffronLight: '#FFF6DF',
              crimson: '#B91C1C'
            }
          },
          fontFamily: {
            serif: ['Fraunces', 'Georgia', 'serif'],
            sans: ['Plus Jakarta Sans', 'system-ui', 'sans-serif'],
            mono: ['JetBrains Mono', 'monospace']
          }
        }
      }
    }
  </script>
  <style>
    /* STRICT 90-DEGREE SWISS ARCHITECTURAL OVERRIDE */
    *, *::before, *::after {
      border-radius: 0px !important;
      box-sizing: border-box;
    }

    html {
      scroll-behavior: smooth;
      background-color: #F4F1EA;
      color: #111111;
    }

    /* Architectural Exposed Grid Backdrop */
    body {
      background-color: #F4F1EA;
      background-image:
        linear-gradient(to right, rgba(17, 17, 17, 0.06) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(17, 17, 17, 0.06) 1px, transparent 1px);
      background-size: 48px 48px;
      overflow-x: hidden;
    }

    /* Offset Solid Block Shadows */
    .shadow-hard {
      box-shadow: 6px 6px 0px #111111;
    }
    .shadow-hard-sm {
      box-shadow: 4px 4px 0px #111111;
    }
    .shadow-hard-emerald {
      box-shadow: 6px 6px 0px #004E36;
    }
    .shadow-hard-saffron {
      box-shadow: 4px 4px 0px #E5A000;
    }

    /* Tactile Sharp Button Press Mechanics */
    .btn-rect {
      transition: transform 0.1s ease, box-shadow 0.1s ease, background-color 0.12s ease, color 0.12s ease;
    }
    .btn-rect:hover {
      transform: translate(-1px, -1px);
    }
    .btn-rect:active {
      transform: translate(3px, 3px);
      box-shadow: 1px 1px 0px #111111 !important;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 10px;
      height: 10px;
    }
    ::-webkit-scrollbar-track {
      background: #F4F1EA;
      border-left: 2px solid #111111;
    }
    ::-webkit-scrollbar-thumb {
      background: #004E36;
      border: 2px solid #111111;
    }
  </style>
</head>
<body class="font-sans antialiased selection:bg-wf-saffron selection:text-wf-ink">

  <!-- ===================================================================== -->
  <!-- STICKY ARCHITECTURAL NAVIGATION BAR                                   -->
  <!-- ===================================================================== -->
  <header class="sticky top-0 z-50 bg-wf-paper border-b-2 border-wf-ink">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-wrap items-stretch justify-between">
      
      <!-- Brand Identity Logo Cell -->
      <a href="#hero" class="py-3 pr-6 flex items-center gap-3 border-r-2 border-wf-ink group">
        <svg viewBox="0 0 340 66" class="h-11 w-auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Whole Foods Market">
          <!-- Leafy Sprout over 'O' in WHOLE -->
          <path d="M84 13 C79 5, 69 5, 65 12 C71 11, 78 13, 82 17 C76 14, 68 15, 63 20 C70 19, 79 19, 86 22 Z" fill="#004E36"/>
          <path d="M84 13 C88 6, 95 7, 98 12 C92 12, 87 14, 85 20 Z" fill="#004E36"/>
          <text x="4" y="42" font-family="Fraunces, Georgia, serif" font-weight="800" font-size="34" letter-spacing="-0.8" fill="#111111">WHOLE FOODS</text>
          <rect x="6" y="48" width="324" height="14" fill="#004E36"/>
          <text x="168" y="58.5" text-anchor="middle" font-family="JetBrains Mono, monospace" font-weight="700" font-size="9.5" letter-spacing="11" fill="#FFFFFF">MARKET</text>
        </svg>
      </a>

      <!-- 4-Module Rectangular Navigation Matrix -->
      <nav class="hidden lg:flex items-center py-2 px-4 flex-1 justify-center">
        <div class="grid grid-cols-4 border-2 border-wf-ink bg-white w-full max-w-xl">
          <button onclick="scrollToModule('mythbuster')" id="nav-mythbuster" class="nav-tab py-2 px-3 font-mono text-[11px] font-bold tracking-wider uppercase border-r-2 border-wf-ink bg-wf-emerald text-white transition-colors">
            01.<br>MYTHBUSTER
          </button>
          <button onclick="scrollToModule('ledger')" id="nav-ledger" class="nav-tab py-2 px-3 font-mono text-[11px] font-bold tracking-wider uppercase border-r-2 border-wf-ink bg-white text-wf-ink hover:bg-wf-emeraldLight transition-colors flex items-center justify-center gap-1.5">
            <span>02. LIVE<br>RECEIPT</span>
            <span id="nav-basket-badge" class="bg-wf-saffron text-wf-ink border border-wf-ink px-1.5 py-0.5 text-[10px] font-extrabold">6</span>
          </button>
          <button onclick="scrollToModule('architect')" id="nav-architect" class="nav-tab py-2 px-3 font-mono text-[11px] font-bold tracking-wider uppercase border-r-2 border-wf-ink bg-white text-wf-ink hover:bg-wf-emeraldLight transition-colors">
            03. MEAL<br>ARCHITECT
          </button>
          <button onclick="scrollToModule('economics')" id="nav-economics" class="nav-tab py-2 px-3 font-mono text-[11px] font-bold tracking-wider uppercase bg-white text-wf-ink hover:bg-wf-emeraldLight transition-colors">
            04. AUDIT<br>LEDGER
          </button>
        </div>
      </nav>

      <!-- Global Prime Reset Switch & Export Action -->
      <div class="flex items-stretch border-l-2 border-wf-ink">
        <!-- Interactive Prime Toggle Cell -->
        <button id="prime-toggle-btn" onclick="togglePrimeMode()" class="px-4 py-2 bg-wf-paper hover:bg-wf-saffronLight border-r-2 border-wf-ink flex items-center gap-3 text-left group">
          <div id="prime-square-indicator" class="w-8 h-8 border-2 border-wf-ink bg-wf-saffron flex items-center justify-center font-mono text-[11px] font-extrabold text-wf-ink shadow-hard-sm">
            ON
          </div>
          <div>
            <div class="flex items-center gap-1.5">
              <span class="font-mono text-[11px] font-extrabold uppercase tracking-wider text-wf-ink">PRIME RESET</span>
              <span id="prime-discount-pill" class="bg-wf-emerald text-white font-mono text-[9px] font-bold px-1 py-0.5">-10%</span>
            </div>
            <div class="font-mono text-[9px] text-neutral-500 uppercase tracking-wider">EXTRA MEMBER PRICING</div>
          </div>
        </button>

        <!-- Direct Receipt .TXT Export Cell -->
        <div class="p-2 flex items-center">
          <button onclick="exportReceiptTxt()" class="btn-rect bg-wf-emerald hover:bg-wf-emeraldDark text-white border-2 border-wf-ink shadow-hard-sm px-4 py-2 font-mono text-[11px] font-bold uppercase tracking-wider flex items-center gap-2">
            <span>⇣</span>
            <span>EXPORT<br>.TXT</span>
          </button>
        </div>
      </div>

    </div>
  </header>

  <!-- ===================================================================== -->
  <!-- HERO ARCHITECTURAL EDITORIAL FRAME                                    -->
  <!-- ===================================================================== -->
  <section id="hero" class="max-w-7xl mx-auto px-4 sm:px-6 pt-6 pb-8">
    <div class="bg-wf-paper border-2 border-wf-ink shadow-hard grid grid-cols-1 lg:grid-cols-12">
      
      <!-- Left 8 Columns: Editorial Manifesto -->
      <div class="lg:col-span-8 p-6 sm:p-10 lg:p-12 border-b-2 lg:border-b-0 lg:border-r-2 border-wf-ink flex flex-col justify-between">
        <div>
          <div class="inline-flex items-center gap-2 bg-wf-saffronLight border-2 border-wf-ink px-3 py-1.5 mb-6">
            <span class="w-2.5 h-2.5 bg-wf-emerald inline-block"></span>
            <span class="font-mono text-[11px] font-bold tracking-widest uppercase text-wf-ink">
              CASE STUDY 01 // RETIRING THE "WHOLE PAYCHECK" STEREOTYPE
            </span>
          </div>

          <h1 class="font-serif font-extrabold text-4xl sm:text-5xl lg:text-[54px] leading-[1.06] tracking-tight text-wf-ink mb-6">
            Uncompromising Quality.<br>
            <span class="inline-block bg-wf-emerald text-white px-3 py-1 mt-1 border-2 border-wf-ink">
              Reset Everyday Prices.
            </span>
          </h1>

          <p class="text-base sm:text-lg text-neutral-700 leading-relaxed max-w-2xl mb-8">
            The perception that Whole Foods Market is out of reach belongs to 2015.
            Through <strong class="text-wf-ink font-bold">365 by Whole Foods Market™</strong> direct-farm volume and Prime supply-chain precision, our foundational organic staples now beat or match conventional supermarkets—while still banning <strong class="text-wf-ink font-bold">500+ synthetic additives</strong>.
          </p>
        </div>

        <div class="flex flex-wrap gap-4 pt-2">
          <button onclick="scrollToModule('ledger')" class="btn-rect bg-wf-emerald hover:bg-wf-emeraldDark text-white border-2 border-wf-ink shadow-hard-sm px-6 py-3.5 font-mono text-xs font-bold uppercase tracking-wider flex items-center gap-3">
            <span>OPEN INTERACTIVE RECEIPT CALCULATOR</span>
            <span>↘</span>
          </button>
          <button onclick="scrollToModule('architect')" class="btn-rect bg-white hover:bg-wf-saffronLight text-wf-ink border-2 border-wf-ink shadow-hard-sm px-6 py-3.5 font-mono text-xs font-bold uppercase tracking-wider">
            EXPLORE $35 MEAL ARCHITECT
          </button>
        </div>
      </div>

      <!-- Right 4 Columns: 3-Stack Telemetry Metrics -->
      <div class="lg:col-span-4 grid grid-rows-3 divide-y-2 divide-wf-ink">
        <!-- Metric 01 -->
        <div class="p-6 sm:p-7 bg-wf-paper flex flex-col justify-center">
          <div class="font-mono text-[10px] font-bold tracking-widest uppercase text-neutral-500 mb-2">
            METRIC 01 // BASKET DELTA
          </div>
          <div class="flex items-baseline gap-2.5 mb-2">
            <span id="hero-metric-delta" class="font-mono font-extrabold text-3xl sm:text-4xl text-wf-emerald">-27.4%</span>
            <span class="bg-wf-saffron border border-wf-ink px-2 py-0.5 font-mono text-[10px] font-extrabold uppercase text-wf-ink">VERIFIED</span>
          </div>
          <p class="text-xs text-neutral-600 leading-relaxed">
            Average reduction compared to public price perception on weekly staples.
          </p>
        </div>

        <!-- Metric 02 -->
        <div class="p-6 sm:p-7 bg-wf-paper flex flex-col justify-center">
          <div class="font-mono text-[10px] font-bold tracking-widest uppercase text-neutral-500 mb-2">
            METRIC 02 // 365™ CATALOG
          </div>
          <div class="flex items-baseline gap-2 mb-2">
            <span class="font-mono font-extrabold text-3xl sm:text-4xl text-wf-ink">420+</span>
            <span class="font-mono text-xs font-bold uppercase text-wf-emerald">UNDER $3.00</span>
          </div>
          <p class="text-xs text-neutral-600 leading-relaxed">
            Everyday pantry, produce, and dairy items locked below three dollars.
          </p>
        </div>

        <!-- Metric 03 -->
        <div class="p-6 sm:p-7 bg-wf-emerald text-white flex flex-col justify-center">
          <div class="font-mono text-[10px] font-bold tracking-widest uppercase text-wf-saffron mb-2">
            METRIC 03 // QUALITY STANDARD
          </div>
          <div class="flex items-baseline gap-2 mb-2">
            <span class="font-mono font-extrabold text-3xl sm:text-4xl text-white">0.00%</span>
            <span class="font-mono text-xs font-bold uppercase text-wf-saffron">COMPROMISE</span>
          </div>
          <p class="text-xs text-emerald-100 leading-relaxed">
            Zero artificial flavors, hydrogenated fats, or high-fructose corn syrup allowed.
          </p>
        </div>
      </div>

    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- MODULE 01: 5-SQUARE MYTHBUSTER MATRIX & SKU INSPECTOR                 -->
  <!-- ===================================================================== -->
  <section id="mythbuster" class="max-w-7xl mx-auto px-4 sm:px-6 py-6">
    <div class="border-2 border-wf-ink shadow-hard bg-wf-paper">
      
      <!-- Top Black Banner Header -->
      <div class="bg-wf-ink text-white px-6 py-4 border-b-2 border-wf-ink flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
          <span class="bg-wf-saffron text-wf-ink font-mono text-[11px] font-extrabold px-2.5 py-1 uppercase tracking-wider border border-wf-ink">
            INTERACTIVE AUDIT
          </span>
          <h2 class="font-serif font-bold text-xl sm:text-2xl text-white">
            Select Any Square Staple to Inspect Myth vs. 2026 Reset Reality
          </h2>
        </div>
        <div class="font-mono text-[11px] text-wf-saffron uppercase tracking-widest">
          CLICK ANY SQUARE TILE BELOW [01 — 05]
        </div>
      </div>

      <!-- 5-Square Interactive Tile Matrix -->
      <div id="myth-tiles-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 divide-y-2 sm:divide-y-0 sm:divide-x-2 divide-wf-ink border-b-2 border-wf-ink">
        <!-- Populated dynamically via JS -->
      </div>

      <!-- Detailed SKU Inspector & Live Discrepancy Bar Chart -->
      <div id="myth-inspector-panel" class="grid grid-cols-1 lg:grid-cols-12 divide-y-2 lg:divide-y-0 lg:divide-x-2 divide-wf-ink">
        <!-- Populated dynamically via JS -->
      </div>

    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- MODULE 02: INTERACTIVE GROCERY LEDGER & THERMAL RECEIPT               -->
  <!-- ===================================================================== -->
  <section id="ledger" class="max-w-7xl mx-auto px-4 sm:px-6 py-8">
    
    <!-- Module Header Box -->
    <div class="bg-wf-paper border-2 border-wf-ink shadow-hard p-6 sm:p-8 mb-8">
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b-2 border-wf-ink">
        <div>
          <div class="font-mono text-[11px] font-bold tracking-widest uppercase text-wf-emerald mb-2">
            MODULE 02 // LIVE QUANTITY & RECEIPT ENGINE
          </div>
          <h2 class="font-serif font-extrabold text-3xl sm:text-4xl text-wf-ink mb-2">
            Interactive Grocery Ledger &<br>Thermal Receipt
          </h2>
          <p class="text-sm text-neutral-600 max-w-xl">
            Adjust quantities with the square <code class="font-mono font-bold text-wf-ink">[-]</code> and <code class="font-mono font-bold text-wf-ink">[+]</code> buttons or load a preset basket. Every modification recalculates your live receipt, bar chart, and 52-week savings projection.
          </p>
        </div>

        <!-- Preset Load Buttons -->
        <div class="flex flex-wrap gap-2.5">
          <button onclick="loadPreset('essentials')" id="preset-essentials" class="btn-rect bg-wf-emerald text-white border-2 border-wf-ink shadow-hard-sm px-4 py-2.5 font-mono text-[11px] font-bold uppercase tracking-wider">
            [ LOAD: WEEKLY ESSENTIALS ]
          </button>
          <button onclick="loadPreset('college')" id="preset-college" class="btn-rect bg-wf-saffron text-wf-ink border-2 border-wf-ink shadow-hard-sm px-4 py-2.5 font-mono text-[11px] font-bold uppercase tracking-wider">
            [ LOAD: COLLEGE FUEL ]
          </button>
          <button onclick="loadPreset('family')" id="preset-family" class="btn-rect bg-white hover:bg-wf-emeraldLight text-wf-ink border-2 border-wf-ink shadow-hard-sm px-4 py-2.5 font-mono text-[11px] font-bold uppercase tracking-wider">
            [ LOAD: FAMILY HAUL ]
          </button>
          <button onclick="clearBasket()" class="btn-rect bg-white hover:bg-red-50 text-wf-crimson border-2 border-wf-ink shadow-hard-sm px-4 py-2.5 font-mono text-[11px] font-bold uppercase tracking-wider">
            [ CLEAR ]
          </button>
        </div>
      </div>

      <!-- Category Filter Tabs & Active Counter -->
      <div class="pt-5 flex flex-wrap items-center justify-between gap-4">
        <div id="category-tabs" class="inline-flex flex-wrap border-2 border-wf-ink bg-white">
          <!-- Populated by JS -->
        </div>
        <div class="border-2 border-wf-ink bg-wf-alabaster px-4 py-2 font-mono text-xs font-bold uppercase tracking-wider">
          ACTIVE UNITS IN BASKET: <span id="active-unit-count" class="text-wf-emerald font-extrabold">6</span>
        </div>
      </div>
    </div>

    <!-- Main 2-Column Split: Catalog Cards (Left) + Live Thermal Receipt (Right) -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
      
      <!-- Left 7 Columns: 12-Item Illustrated Catalog Grid -->
      <div id="catalog-grid" class="lg:col-span-7 grid grid-cols-1 sm:grid-cols-2 gap-6">
        <!-- Populated by JS -->
      </div>

      <!-- Right 5 Columns: Live Thermal Receipt Ledger -->
      <div class="lg:col-span-5 lg:sticky lg:top-20">
        <div class="bg-wf-paper border-2 border-wf-ink shadow-hard">
          
          <!-- Receipt Green Header -->
          <div class="bg-wf-emerald text-white p-6 border-b-2 border-wf-ink">
            <div class="flex justify-between items-center font-mono text-[10px] tracking-widest uppercase text-wf-saffron mb-2">
              <span>STORE #104 // CHARLOTTE NC</span>
              <span>AUDIT: 2026-RESET</span>
            </div>
            <h3 class="font-serif font-extrabold text-2xl tracking-tight text-white">
              WHOLE FOODS MARKET LEDGER
            </h3>
            <p class="font-mono text-[11px] text-emerald-100 uppercase tracking-wider mt-1">
              365™ EVERYDAY VALUE VS. CONVENTIONAL GROCER
            </p>
          </div>

          <!-- 3-Tier Summary Bar Comparison -->
          <div class="p-5 bg-wf-alabaster border-b-2 border-wf-ink font-mono text-xs space-y-2">
            <div class="flex justify-between items-center">
              <span class="text-neutral-500">2018 MYTH ESTIMATE:</span>
              <span id="receipt-myth-total" class="text-wf-crimson line-through font-bold">$33.24</span>
            </div>
            <div class="flex justify-between items-center">
              <span class="text-neutral-600">AVG SUPERMARKET:</span>
              <span id="receipt-conv-total" class="text-wf-ink font-bold">$20.64</span>
            </div>
            <div class="flex justify-between items-center text-sm">
              <span class="text-wf-emerald font-extrabold">WHOLE FOODS RESET:</span>
              <span id="receipt-wf-total" class="text-wf-emerald font-extrabold">$14.96</span>
            </div>
            <!-- Dual Ratio Bar -->
            <div class="w-full h-3.5 border-2 border-wf-ink bg-wf-saffron flex overflow-hidden mt-2">
              <div id="receipt-ratio-bar" class="bg-wf-emerald h-full transition-all duration-300" style="width: 72%;"></div>
            </div>
          </div>

          <!-- Itemized Receipt Table Header -->
          <div class="bg-wf-ink text-white px-5 py-2.5 font-mono text-[10px] font-bold uppercase tracking-widest flex justify-between">
            <span>ITEM / QTY</span>
            <div class="flex gap-6">
              <span>AVG GROCER</span>
              <span class="text-wf-saffron">WF RESET</span>
            </div>
          </div>

          <!-- Itemized Line Items Container -->
          <div id="receipt-line-items" class="p-5 divide-y divide-neutral-300 max-h-80 overflow-y-auto font-mono text-xs">
            <!-- Populated by JS -->
          </div>

          <!-- Savings Totals Footer -->
          <div class="p-5 bg-wf-emeraldLight border-t-2 border-wf-ink font-mono">
            <div class="flex justify-between items-center text-xs font-bold text-wf-ink mb-2">
              <span>WEEKLY BASKET SAVINGS:</span>
              <span id="receipt-weekly-saved" class="text-wf-emerald text-base font-extrabold">$5.68</span>
            </div>
            <div class="flex justify-between items-center bg-wf-emerald text-white p-3 border-2 border-wf-ink">
              <span class="text-[11px] font-bold uppercase tracking-wider">52-WEEK ANNUALIZED SAVINGS:</span>
              <span id="receipt-annual-saved" class="text-wf-saffron text-lg font-extrabold">$295.36/YR</span>
            </div>

            <!-- Action Buttons on Receipt -->
            <div class="grid grid-cols-2 gap-3 mt-4">
              <button onclick="copyReceiptSummary()" class="btn-rect bg-white hover:bg-wf-saffronLight text-wf-ink border-2 border-wf-ink shadow-hard-sm py-2.5 px-3 font-mono text-[11px] font-bold uppercase tracking-wider">
                [ COPY AUDIT ]
              </button>
              <button onclick="exportReceiptTxt()" class="btn-rect bg-wf-ink hover:bg-wf-emerald text-white border-2 border-wf-ink shadow-hard-sm py-2.5 px-3 font-mono text-[11px] font-bold uppercase tracking-wider">
                [ DOWNLOAD .TXT ]
              </button>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- MODULE 03: $35 BUDGET MEAL ARCHITECT                                  -->
  <!-- ===================================================================== -->
  <section id="architect" class="max-w-7xl mx-auto px-4 sm:px-6 py-8">
    <div class="bg-wf-paper border-2 border-wf-ink shadow-hard p-6 sm:p-8">
      
      <!-- Header & Portion Scaling Controls -->
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6 pb-6 border-b-2 border-wf-ink">
        <div>
          <div class="font-mono text-[11px] font-bold tracking-widest uppercase text-wf-emerald mb-2">
            MODULE 03 // SHOPPABLE CULINARY BLUEPRINTS
          </div>
          <h2 class="font-serif font-extrabold text-3xl sm:text-4xl text-wf-ink mb-2">
            The $35 Budget Meal Architect
          </h2>
          <p class="text-sm text-neutral-600 max-w-xl">
            Every recipe is priced down to the exact cent using real <strong class="text-wf-ink">365 by Whole Foods Market™</strong> SKUs. Scale portions between 2 and 4 servings or load all ingredients straight into your live receipt above.
          </p>
        </div>

        <!-- Portion Scale + Diet Filter -->
        <div class="flex flex-wrap items-center gap-4">
          <div class="inline-flex border-2 border-wf-ink bg-white">
            <button onclick="setServings(2)" id="scale-2-btn" class="px-4 py-2 font-mono text-xs font-bold uppercase bg-wf-emerald text-white border-r-2 border-wf-ink">
              2 SERVINGS
            </button>
            <button onclick="setServings(4)" id="scale-4-btn" class="px-4 py-2 font-mono text-xs font-bold uppercase bg-white text-wf-ink hover:bg-wf-emeraldLight">
              4 SERVINGS
            </button>
          </div>

          <div id="diet-filter-bar" class="inline-flex flex-wrap border-2 border-wf-ink bg-white">
            <!-- Populated by JS -->
          </div>
        </div>
      </div>

      <!-- Meal Architect Grid -->
      <div id="meal-grid" class="grid grid-cols-1 md:grid-cols-3 gap-6 pt-8">
        <!-- Populated by JS -->
      </div>

    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- MODULE 04: STRUCTURAL AUDIT LEDGER (SUPPLY CHAIN TRANSPARENCY)        -->
  <!-- ===================================================================== -->
  <section id="economics" class="max-w-7xl mx-auto px-4 sm:px-6 py-8 pb-16">
    <div class="bg-wf-paper border-2 border-wf-ink shadow-hard p-6 sm:p-8">
      <div class="border-b-2 border-wf-ink pb-6 mb-8 flex flex-col md:flex-row md:items-end justify-between gap-4">
        <div>
          <div class="font-mono text-[11px] font-bold tracking-widest uppercase text-wf-emerald mb-2">
            MODULE 04 // SUPPLY CHAIN ECONOMICS LEDGER
          </div>
          <h2 class="font-serif font-extrabold text-3xl sm:text-4xl text-wf-ink">
            How We Engineered Lower Prices Without Lowering Standards
          </h2>
        </div>
        <span class="bg-wf-saffron border-2 border-wf-ink px-3 py-1.5 font-mono text-xs font-extrabold uppercase">
          ZERO QUALITY DILUTION
        </span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="border-2 border-wf-ink bg-white p-6 shadow-hard-sm">
          <div class="font-mono text-xs font-bold text-wf-emerald uppercase mb-2">01 // DIRECT FARM CONTRACTS</div>
          <div class="font-serif font-extrabold text-3xl text-wf-ink mb-3">-24% Broker Markup</div>
          <p class="text-sm text-neutral-600 leading-relaxed">
            By contracting multi-year harvests directly with Certified Humane® and USDA Organic cooperatives, we bypass three layers of regional wholesale middlemen.
          </p>
        </div>

        <div class="border-2 border-wf-ink bg-white p-6 shadow-hard-sm">
          <div class="font-mono text-xs font-bold text-wf-emerald uppercase mb-2">02 // PRIME COLD-CHAIN SCALE</div>
          <div class="font-serif font-extrabold text-3xl text-wf-ink mb-3">-19% Freight Cost</div>
          <p class="text-sm text-neutral-600 leading-relaxed">
            Unified regional distribution hubs and automated demand forecasting cut cold-storage transit waste across 500+ North American stores.
          </p>
        </div>

        <div class="border-2 border-wf-ink bg-wf-emerald text-white p-6 shadow-hard-sm">
          <div class="font-mono text-xs font-bold text-wf-saffron uppercase mb-2">03 // 500+ BANNED INGREDIENTS</div>
          <div class="font-serif font-extrabold text-3xl text-white mb-3">100% Clean Label</div>
          <p class="text-sm text-emerald-100 leading-relaxed">
            Every price reset item still enforces our strict quality floor: zero hydrogenated fats, zero high-fructose corn syrup, and zero artificial sweeteners.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===================================================================== -->
  <!-- FOOTER                                                                -->
  <!-- ===================================================================== -->
  <footer class="bg-wf-ink text-white border-t-2 border-wf-ink py-8">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 flex flex-col sm:flex-row items-center justify-between gap-4 font-mono text-xs">
      <div>
        WHOLE FOODS MARKET — PRICE IMAGE RESET // HAVK WEB DEVELOPMENT COMPETITION
      </div>
      <div class="text-wf-saffron font-bold">
        DESIGNED & ENGINEERED BY PULKIT TOMAR (UNC CHARLOTTE)
      </div>
    </div>
  </footer>

  <!-- ===================================================================== -->
  <!-- CULINARY BLUEPRINT MODAL                                              -->
  <!-- ===================================================================== -->
  <div id="recipe-modal" class="fixed inset-0 z-50 bg-black/70 hidden items-center justify-center p-4">
    <div class="bg-wf-paper border-2 border-wf-ink shadow-hard max-w-xl w-full p-6 sm:p-8">
      <div class="flex justify-between items-start border-b-2 border-wf-ink pb-4 mb-4">
        <div>
          <div id="modal-code" class="font-mono text-xs font-bold text-wf-emerald uppercase"></div>
          <h3 id="modal-title" class="font-serif font-extrabold text-2xl text-wf-ink mt-1"></h3>
        </div>
        <button onclick="closeRecipeModal()" class="btn-rect bg-wf-ink text-white px-3 py-1 font-mono text-xs font-bold">
          [ X CLOSE ]
        </button>
      </div>
      <div id="modal-steps" class="space-y-3 text-sm text-neutral-800 mb-6"></div>
      <button id="modal-add-btn" class="btn-rect w-full bg-wf-emerald text-white border-2 border-wf-ink shadow-hard-sm py-3 font-mono text-xs font-bold uppercase tracking-wider">
        [ + SYNC ALL INGREDIENTS TO LIVE RECEIPT ]
      </button>
    </div>
  </div>

  <!-- TOAST NOTIFICATION -->
  <div id="toast-box" class="fixed bottom-5 right-5 z-50 bg-wf-ink text-white border-2 border-wf-saffron shadow-hard px-5 py-3 font-mono text-xs font-bold uppercase tracking-wider hidden">
    <span id="toast-text">UPDATED LEDGER</span>
  </div>

  <!-- ===================================================================== -->
  <!-- APPLICATION JAVASCRIPT ENGINE                                         -->
  <!-- ===================================================================== -->
  <script>
    // Global State
    let primeMode = true;
    let activeMythIndex = 0;
    let activeCategory = 'ALL';
    let activeDiet = 'ALL';
    let servingsScale = 2;

    // 12-Item Catalog with Custom Inline SVG Product Illustrations
    const CATALOG = [
      {
        id: 'egg',
        mythTileIndex: 0,
        num: '01',
        sku: '365-EGG-12',
        shortName: 'Cage-Free Eggs',
        fullName: '365™ Large Brown Cage-Free Eggs (12 ct)',
        subline: 'Grade A • Outdoor Perch Access • Zero Antibiotics',
        category: 'DAIRY & EGGS',
        badge: 'CERTIFIED HUMANE',
        badgeType: 'saffron',
        mythPrice: 6.99,
        convPrice: 4.19,
        wfBase: 3.49,
        primePrice: 3.14,
        auditNote: 'Direct regional farm cooperative contracts eliminate 3 layers of wholesale egg broker markups.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M24 6 C15 6 10 18 10 28 C10 38 16 42 24 42 C32 42 38 38 38 28 C38 18 33 6 24 6 Z" fill="#D98A4E" stroke="#111" stroke-width="2.5"/><path d="M18 16 C16 20 15 25 16 30" stroke="#F4C095" stroke-width="2.5" stroke-linecap="square" fill="none"/></svg>`
      },
      {
        id: 'avo',
        mythTileIndex: 1,
        num: '02',
        sku: 'ORG-AVO-04',
        shortName: 'Hass Avocados',
        fullName: 'Organic Hass Avocados Bag (4 Count)',
        subline: 'USDA Organic • Direct Michoacán Grower Co-op',
        category: 'PRODUCE',
        badge: 'WHOLE TRADE®',
        badgeType: 'saffron',
        mythPrice: 7.99,
        convPrice: 4.99,
        wfBase: 3.99,
        primePrice: 3.59,
        auditNote: 'Year-round volume commitments with Michoacán orchards bypass seasonal spot-market surcharges.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M24 6 C16 6 11 17 11 27 C11 36 17 42 24 42 C31 42 37 36 37 27 C37 17 32 6 24 6 Z" fill="#2E6F40" stroke="#111" stroke-width="2.5"/><path d="M24 10 C18 10 14 19 14 27 C14 34 18 39 24 39 C30 39 34 34 34 27 C34 19 30 10 24 10 Z" fill="#A3D95B" stroke="#111" stroke-width="1.5"/><circle cx="24" cy="28" r="6.5" fill="#7C4728" stroke="#111" stroke-width="2"/></svg>`
      },
      {
        id: 'alm',
        mythTileIndex: 2,
        num: '03',
        sku: '365-ALM-64',
        shortName: 'Organic Almondmilk',
        fullName: '365™ Organic Unsweetened Almondmilk (64 oz)',
        subline: 'USDA Organic • Zero Carrageenan • Non-GMO',
        category: 'DAIRY & EGGS',
        badge: 'ZERO CARRAGEENAN',
        badgeType: 'saffron',
        mythPrice: 5.99,
        convPrice: 3.89,
        wfBase: 3.29,
        primePrice: 2.96,
        auditNote: 'In-house 365™ bottling removes national brand marketing overhead while keeping pure organic almonds.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><polygon points="14,16 24,8 34,16" fill="#B8D4E3" stroke="#111" stroke-width="2.5"/><rect x="14" y="16" width="20" height="26" fill="#E8F3F8" stroke="#111" stroke-width="2.5"/><rect x="18" y="23" width="12" height="10" fill="#004E36"/></svg>`
      },
      {
        id: 'beef',
        mythTileIndex: 3,
        num: '04',
        sku: 'beef-gf-16',
        shortName: 'Grass-Fed Beef',
        fullName: '100% Grass-Fed Ground Beef Brick (16 oz)',
        subline: '85/15 Lean • Step-4 Pasture Raised • No Hormones',
        category: 'PROTEIN',
        badge: 'STEP-4 PASTURE',
        badgeType: 'white',
        mythPrice: 10.99,
        convPrice: 7.49,
        wfBase: 6.49,
        primePrice: 5.84,
        auditNote: 'Direct ranch-to-butcher block supply chains lock in pasture-raised pricing below conventional organic beef.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><rect x="9" y="14" width="30" height="22" fill="#D64550" stroke="#111" stroke-width="2.5"/><path d="M14 20 L22 20 M16 26 L28 26 M26 19 L34 23" stroke="#F9EAEB" stroke-width="2.5"/></svg>`
      },
      {
        id: 'bread',
        mythTileIndex: 4,
        num: '05',
        sku: 'BAK-SRD-24',
        shortName: 'Artisan Sourdough',
        fullName: 'San Francisco Sourdough Boule Loaf (24 oz)',
        subline: '24-Hour Wild Ferment • Water, Flour, Sea Salt',
        category: 'PANTRY',
        badge: 'BAKED IN-HOUSE',
        badgeType: 'white',
        mythPrice: 7.49,
        convPrice: 4.99,
        wfBase: 4.29,
        primePrice: 3.86,
        auditNote: 'Scratch-baked daily inside each store bakery—eliminating commercial commissary packaging and freight.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M8 32 C8 18 15 12 24 12 C33 12 40 18 40 32 L8 32 Z" fill="#D99B52" stroke="#111" stroke-width="2.5"/><rect x="8" y="32" width="32" height="6" fill="#B3742E" stroke="#111" stroke-width="2.5"/><path d="M18 18 L22 24 M26 17 L30 23" stroke="#FFF3DF" stroke-width="2.5"/></svg>`
      },
      {
        id: 'spinach',
        mythTileIndex: null,
        num: '06',
        sku: 'ORG-SPN-05',
        shortName: 'Organic Baby Spinach',
        fullName: '365™ Organic Baby Spinach Clamshell (5 oz)',
        subline: 'Triple-Washed • USDA Organic • Cold-Chain Fresh',
        category: 'PRODUCE',
        badge: 'USDA ORGANIC',
        badgeType: 'saffron',
        mythPrice: 4.99,
        convPrice: 3.29,
        wfBase: 2.39,
        primePrice: 2.15,
        auditNote: 'High-velocity regional greenhouse harvesting cuts cold-chain transit time by 48 hours.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M24 8 C12 8 10 22 16 32 C20 38 28 38 32 32 C38 22 36 8 24 8 Z" fill="#1F7A4C" stroke="#111" stroke-width="2.5"/><path d="M24 12 L24 42" stroke="#111" stroke-width="2.5"/></svg>`
      },
      {
        id: 'pasta',
        mythTileIndex: null,
        num: '07',
        sku: '365-PST-16',
        shortName: 'Bronze-Cut Pasta',
        fullName: '365™ Organic Bronze-Die Fusilli Pasta (16 oz)',
        subline: 'Imported Italian Durum Semolina • USDA Organic',
        category: 'PANTRY',
        badge: 'ITALIAN SEMOLINA',
        badgeType: 'white',
        mythPrice: 3.99,
        convPrice: 2.49,
        wfBase: 1.79,
        primePrice: 1.61,
        auditNote: 'Direct container imports from family-run Italian pasta mills under the 365™ private label.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><rect x="13" y="8" width="22" height="32" fill="#F2C14E" stroke="#111" stroke-width="2.5"/><rect x="17" y="15" width="14" height="12" fill="#004E36" stroke="#111" stroke-width="2"/></svg>`
      },
      {
        id: 'tomato',
        mythTileIndex: null,
        num: '08',
        sku: '365-TOM-28',
        shortName: 'Crushed Tomatoes',
        fullName: '365™ Organic San Marzano Style Tomatoes (28 oz)',
        subline: 'BPA-Free Liner • Vine-Ripened California Organic',
        category: 'PANTRY',
        badge: 'BPA-FREE CAN',
        badgeType: 'white',
        mythPrice: 4.49,
        convPrice: 2.99,
        wfBase: 2.19,
        primePrice: 1.97,
        auditNote: 'Packed at peak summer harvest in Sacramento Valley with zero calcium chloride or citric acid.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><circle cx="24" cy="26" r="14" fill="#D93829" stroke="#111" stroke-width="2.5"/><path d="M18 11 L24 15 L30 11 M24 8 L24 15" stroke="#004E36" stroke-width="3"/></svg>`
      },
      {
        id: 'salmon',
        mythTileIndex: null,
        num: '09',
        sku: 'SEA-SLM-12',
        shortName: 'Wild Sockeye Salmon',
        fullName: 'Wild-Caught Alaskan Sockeye Salmon Fillets (12 oz)',
        subline: 'MSC Certified Sustainable • Flash-Frozen at Sea',
        category: 'PROTEIN',
        badge: 'MSC WILD CAUGHT',
        badgeType: 'saffron',
        mythPrice: 15.99,
        convPrice: 12.49,
        wfBase: 9.99,
        primePrice: 8.99,
        auditNote: 'Direct Bristol Bay fishery partnerships eliminate secondary seafood auction fees.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M8 28 C14 14 32 14 40 24 L36 34 C26 34 14 34 8 28 Z" fill="#F27A5E" stroke="#111" stroke-width="2.5"/><path d="M16 21 L20 31 M24 19 L28 32" stroke="#FFE3DC" stroke-width="2"/></svg>`
      },
      {
        id: 'pb',
        mythTileIndex: null,
        num: '10',
        sku: '365-PNB-16',
        shortName: 'Organic Peanut Butter',
        fullName: '365™ Organic Creamy Peanut Butter (16 oz)',
        subline: 'Dry-Roasted Organic Peanuts & Sea Salt Only',
        category: 'PANTRY',
        badge: 'ZERO PALM OIL',
        badgeType: 'saffron',
        mythPrice: 5.99,
        convPrice: 4.29,
        wfBase: 3.29,
        primePrice: 2.96,
        auditNote: 'Two-ingredient roasting in-house under 365™ keeps prices below national natural brands.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><rect x="14" y="10" width="20" height="6" fill="#004E36" stroke="#111" stroke-width="2.5"/><rect x="12" y="16" width="24" height="24" fill="#C88A4B" stroke="#111" stroke-width="2.5"/><rect x="16" y="22" width="16" height="10" fill="#FFFDF9" stroke="#111" stroke-width="1.5"/></svg>`
      },
      {
        id: 'apple',
        mythTileIndex: null,
        num: '11',
        sku: 'ORG-APL-32',
        shortName: 'Honeycrisp Apples',
        fullName: 'Organic Honeycrisp Apples Tote Bag (2 lb)',
        subline: 'Washington State Orchard Direct • Crisp & Sweet',
        category: 'PRODUCE',
        badge: 'WASHINGTON GROWN',
        badgeType: 'white',
        mythPrice: 7.99,
        convPrice: 5.99,
        wfBase: 4.49,
        primePrice: 4.04,
        auditNote: 'Dedicated Yakima Valley orchard rows pre-contracted for Whole Foods Market produce tables.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><path d="M24 14 C16 12 10 18 10 27 C10 36 16 41 24 39 C32 41 38 36 38 27 C38 18 32 12 24 14 Z" fill="#E03C31" stroke="#111" stroke-width="2.5"/><path d="M24 14 L26 7" stroke="#111" stroke-width="2.5"/></svg>`
      },
      {
        id: 'yogurt',
        mythTileIndex: null,
        num: '12',
        sku: '365-YOG-32',
        shortName: 'Greek Strained Yogurt',
        fullName: '365™ Organic Plain Greek Yogurt Tub (32 oz)',
        subline: '18g Protein per Serving • Pasture Dairy • Live Cultures',
        category: 'DAIRY & EGGS',
        badge: '18G PROTEIN',
        badgeType: 'white',
        mythPrice: 6.99,
        convPrice: 5.49,
        wfBase: 4.29,
        primePrice: 3.86,
        auditNote: 'Family-quart format reduces plastic packaging cost per ounce by 31%.',
        svg: `<svg viewBox="0 0 48 48" class="w-9 h-9"><polygon points="10,16 38,16 34,38 14,38" fill="#FFFFFF" stroke="#111" stroke-width="2.5"/><rect x="8" y="12" width="32" height="5" fill="#004E36" stroke="#111" stroke-width="2.5"/></svg>`
      }
    ];

    // Default Basket Quantities (6 items matching your screenshots!)
    let basket = {
      egg: 1,
      avo: 1,
      alm: 1,
      bread: 1,
      spinach: 1,
      pasta: 1
    };

    const PRESETS = {
      essentials: { egg: 1, avo: 1, alm: 1, bread: 1, spinach: 1, pasta: 1 },
      college: { egg: 1, alm: 1, pasta: 2, tomato: 1, pb: 1, apple: 1 },
      family: { egg: 2, avo: 2, alm: 1, beef: 2, bread: 1, spinach: 2, pasta: 2, tomato: 2, salmon: 1, yogurt: 1 }
    };

    const MEALS = [
      {
        id: 'm1',
        code: 'BLUEPRINT 01',
        diet: 'HIGH-PROTEIN',
        title: 'Pan-Seared Wild Sockeye Salmon & Wilted Garlic Spinach',
        time: '18 MIN',
        protein: '42G PROTEIN',
        items: [
          { id: 'salmon', qty: 1 },
          { id: 'spinach', qty: 1 }
        ],
        steps: [
          'Pat Wild-Caught Alaskan Sockeye Salmon fillets dry and season generously with kosher salt & cracked black pepper.',
          'Sear skin-side down in a cast-iron skillet for 4 minutes until crisp; flip for 2 minutes until medium-rare.',
          'Toss 365™ Organic Baby Spinach directly into the warm pan drippings for 90 seconds until wilted.',
          'Serve immediately with fresh lemon wedges.'
        ]
      },
      {
        id: 'm2',
        code: 'BLUEPRINT 02',
        diet: 'HIGH-PROTEIN',
        title: '100% Grass-Fed Beef Bolognese & Bronze-Die Fusilli',
        time: '22 MIN',
        protein: '38G PROTEIN',
        items: [
          { id: 'beef', qty: 1 },
          { id: 'pasta', qty: 1 },
          { id: 'tomato', qty: 1 }
        ],
        steps: [
          'Brown 1 lb 100% Grass-Fed Ground Beef in a heavy pot over high heat for 6 minutes.',
          'Add 28 oz 365™ Organic San Marzano Style Crushed Tomatoes and simmer uncovered for 12 minutes.',
          'Boil 365™ Bronze-Die Organic Fusilli in salted water until al dente.',
          'Toss pasta directly into the ragu so the rough bronze-cut texture locks onto the sauce.'
        ]
      },
      {
        id: 'm3',
        code: 'BLUEPRINT 03',
        diet: 'VEGETARIAN',
        title: 'San Francisco Sourdough Avocado & Cage-Free Egg Tartines',
        time: '10 MIN',
        protein: '24G PROTEIN',
        items: [
          { id: 'bread', qty: 1 },
          { id: 'avo', qty: 1 },
          { id: 'egg', qty: 1 }
        ],
        steps: [
          'Slice thick 1-inch slabs of San Francisco Sourdough Boule and toast until golden brown.',
          'Smash ripe Organic Hass Avocados with flaky sea salt and crushed red pepper.',
          'Poach or fry 365™ Cage-Free Brown Eggs until whites are set and yolks remain jammy.',
          'Stack smashed avocado and warm pasture eggs atop the toasted sourdough.'
        ]
      }
    ];

    // Helper: Get active price for an item
    function getItemPrice(item) {
      return primeMode ? item.primePrice : item.wfBase;
    }

    // =========================================================================
    // RENDER MODULE 01: 5-SQUARE MYTHBUSTER TILES & INSPECTOR
    // =========================================================================
    function renderMythbuster() {
      const topFive = CATALOG.slice(0, 5);
      const tilesContainer = document.getElementById('myth-tiles-container');

      tilesContainer.innerHTML = topFive.map((item, idx) => {
        const isSelected = idx === activeMythIndex;
        const activePrice = getItemPrice(item);
        const bgClass = isSelected ? 'bg-wf-emerald text-white' : 'bg-white text-wf-ink hover:bg-wf-emeraldLight';
        const skuColor = isSelected ? 'text-wf-saffron' : 'text-neutral-500';
        const mythColor = isSelected ? 'text-emerald-200' : 'text-neutral-400';
        const labelColor = isSelected ? 'text-wf-saffron' : 'text-wf-emerald';
        const priceColor = isSelected ? 'text-white' : 'text-wf-ink';

        return `
          <button onclick="selectMythTile(${idx})" class="p-5 text-left flex flex-col justify-between min-h-[175px] transition-colors ${bgClass}">
            <div class="w-full flex items-start justify-between gap-2 mb-3">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider ${skuColor}">
                ${item.num} // ${item.sku}
              </span>
              <div class="w-9 h-9 flex-shrink-0 flex items-center justify-center">
                ${item.svg}
              </div>
            </div>
            <div class="mb-4">
              <div class="font-serif font-bold text-base leading-snug">${item.shortName}</div>
              <div class="font-mono text-[10px] line-through ${mythColor} mt-0.5">MYTH: $${item.mythPrice.toFixed(2)}</div>
            </div>
            <div class="w-full flex items-baseline justify-between pt-2 border-t ${isSelected ? 'border-emerald-700' : 'border-neutral-200'}">
              <span class="font-mono text-[10px] font-bold uppercase tracking-wider ${labelColor}">RESET PRICE</span>
              <span class="font-mono font-extrabold text-xl ${priceColor}">$${activePrice.toFixed(2)}</span>
            </div>
          </button>
        `;
      }).join('');

      // Render Inspector Panel below the 5 tiles
      const item = topFive[activeMythIndex];
      const activePrice = getItemPrice(item);
      const convPct = Math.round((item.convPrice / item.mythPrice) * 100);
      const wfPct = Math.round((activePrice / item.mythPrice) * 100);
      const pctBelowMyth = Math.round(((item.mythPrice - activePrice) / item.mythPrice) * 100);
      const cheaperThanConv = (item.convPrice - activePrice).toFixed(2);

      const inspector = document.getElementById('myth-inspector-panel');
      inspector.innerHTML = `
        <!-- Left 5 Cols: SKU Spec Card -->
        <div class="lg:col-span-5 p-6 sm:p-8 flex flex-col justify-between bg-wf-paper">
          <div>
            <div class="flex items-center justify-between gap-2 pb-4 mb-5 border-b border-neutral-300">
              <span class="font-mono text-[11px] text-neutral-600 uppercase tracking-wider">
                SKU #${item.sku} // ${item.category}
              </span>
              <span class="bg-wf-emerald text-white font-mono text-[10px] font-bold px-2.5 py-1 uppercase tracking-wider">
                ${item.badge}
              </span>
            </div>

            <div class="flex items-start gap-4 mb-6">
              <div class="w-16 h-16 border-2 border-wf-ink bg-white shadow-hard-sm flex-shrink-0 flex items-center justify-center">
                ${item.svg}
              </div>
              <div>
                <h3 class="font-serif font-extrabold text-2xl text-wf-ink leading-snug">
                  ${item.fullName}
                </h3>
                <p class="font-mono text-[11px] text-neutral-500 mt-1">
                  ${item.subline}
                </p>
              </div>
            </div>

            <div class="border-2 border-wf-ink bg-white p-4 mb-6">
              <p class="text-sm text-neutral-700 leading-relaxed">
                ${item.auditNote}
              </p>
            </div>
          </div>

          <button onclick="addItemToReceipt('${item.id}')" class="btn-rect w-full bg-wf-emerald hover:bg-wf-emeraldDark text-white border-2 border-wf-ink shadow-hard-sm py-3.5 px-4 font-mono text-xs font-bold uppercase tracking-wider flex items-center justify-center gap-2">
            <span class="text-wf-saffron">⊞</span>
            <span>[ + ADD ITEM TO LIVE RECEIPT BELOW ]</span>
          </button>
        </div>

        <!-- Right 7 Cols: 3-Tier Horizontal Bar Comparison -->
        <div class="lg:col-span-7 p-6 sm:p-8 bg-wf-paper flex flex-col justify-between">
          <div class="flex flex-wrap items-center justify-between gap-2 pb-4 mb-5 border-b border-neutral-300">
            <span class="font-mono text-xs font-bold uppercase tracking-wider text-wf-ink">
              LIVE PRICE DISCREPANCY INDEX
            </span>
            <span class="bg-wf-saffron border border-wf-ink text-wf-ink font-mono text-[10px] font-extrabold px-2.5 py-1 uppercase">
              ${primeMode ? 'PRIME MEMBER RATE (-10% ACTIVE)' : 'STANDARD 365™ RESET RATE'}
            </span>
          </div>

          <div class="space-y-4">
            <!-- Bar 01: Public Myth -->
            <div class="border border-neutral-300 bg-white p-4">
              <div class="flex justify-between items-baseline mb-2">
                <span class="font-mono text-[11px] font-bold uppercase text-neutral-600">
                  01 // PUBLIC "WHOLE PAYCHECK" ASSUMPTION
                </span>
                <span class="font-mono text-lg font-extrabold text-wf-crimson line-through">
                  $${item.mythPrice.toFixed(2)}
                </span>
              </div>
              <div class="w-full h-3.5 border border-wf-ink bg-neutral-100">
                <div class="h-full bg-wf-crimson" style="width: 100%;"></div>
              </div>
            </div>

            <!-- Bar 02: Conventional Supermarket -->
            <div class="border border-neutral-300 bg-white p-4">
              <div class="flex justify-between items-baseline mb-2">
                <span class="font-mono text-[11px] font-bold uppercase text-neutral-600">
                  02 // STANDARD CONVENTIONAL SUPERMARKET AVG
                </span>
                <span class="font-mono text-lg font-extrabold text-wf-ink">
                  $${item.convPrice.toFixed(2)}
                </span>
              </div>
              <div class="w-full h-3.5 border border-wf-ink bg-neutral-100">
                <div class="h-full bg-neutral-500" style="width: ${convPct}%;"></div>
              </div>
            </div>

            <!-- Bar 03: Actual Whole Foods 2026 Reset Price -->
            <div class="border-2 border-wf-emerald bg-wf-emeraldLight p-4 shadow-hard-emerald">
              <div class="flex justify-between items-baseline mb-2">
                <span class="font-mono text-xs font-extrabold uppercase text-wf-emerald flex items-center gap-2">
                  <span class="w-2.5 h-2.5 bg-wf-emerald inline-block"></span>
                  <span>03 // ACTUAL WHOLE FOODS 2026 RESET PRICE</span>
                </span>
                <span class="font-mono text-2xl font-extrabold text-wf-emerald">
                  $${activePrice.toFixed(2)}
                </span>
              </div>
              <div class="w-full h-4 border-2 border-wf-ink bg-white mb-2.5">
                <div class="h-full bg-wf-emerald transition-all duration-300" style="width: ${wfPct}%;"></div>
              </div>
              <div class="flex flex-wrap justify-between items-center font-mono text-[11px] font-bold uppercase">
                <span class="text-wf-ink">VERIFIED SAVINGS: ${pctBelowMyth}% BELOW STEREOTYPE</span>
                <span class="text-wf-emerald">$${cheaperThanConv} CHEAPER THAN STANDARD GROCER</span>
              </div>
            </div>
          </div>
        </div>
      `;
    }

    function selectMythTile(idx) {
      activeMythIndex = idx;
      renderMythbuster();
    }

    // =========================================================================
    // RENDER MODULE 02: CATEGORY TABS, 12-ITEM CATALOG & THERMAL RECEIPT
    // =========================================================================
    function renderCategoryTabs() {
      const counts = {
        'ALL': CATALOG.length,
        'PRODUCE': CATALOG.filter(i => i.category === 'PRODUCE').length,
        'DAIRY & EGGS': CATALOG.filter(i => i.category === 'DAIRY & EGGS').length,
        'PANTRY': CATALOG.filter(i => i.category === 'PANTRY').length,
        'PROTEIN': CATALOG.filter(i => i.category === 'PROTEIN').length
      };

      const labels = [
        { key: 'ALL', text: `ALL ITEMS (${counts['ALL']})` },
        { key: 'PRODUCE', text: `PRODUCE (${counts['PRODUCE']})` },
        { key: 'DAIRY & EGGS', text: `DAIRY & EGGS (${counts['DAIRY & EGGS']})` },
        { key: 'PANTRY', text: `PANTRY (${counts['PANTRY']})` },
        { key: 'PROTEIN', text: `PROTEIN (${counts['PROTEIN']})` }
      ];

      const container = document.getElementById('category-tabs');
      container.innerHTML = labels.map((tab, idx) => {
        const isActive = activeCategory === tab.key;
        const borderRight = idx < labels.length - 1 ? 'border-r-2 border-wf-ink' : '';
        const styleClass = isActive
          ? 'bg-wf-ink text-white'
          : 'bg-white text-wf-ink hover:bg-wf-emeraldLight';
        return `
          <button onclick="setCategory('${tab.key}')" class="px-4 py-2 font-mono text-[11px] font-bold uppercase tracking-wider transition-colors ${borderRight} ${styleClass}">
            ${tab.text}
          </button>
        `;
      }).join('');
    }

    function setCategory(cat) {
      activeCategory = cat;
      renderCategoryTabs();
      renderCatalogAndReceipt();
    }

    function renderCatalogAndReceipt() {
      const filtered = activeCategory === 'ALL'
        ? CATALOG
        : CATALOG.filter(item => item.category === activeCategory);

      const grid = document.getElementById('catalog-grid');
      grid.innerHTML = filtered.map(item => {
        const qty = basket[item.id] || 0;
        const unitPrice = getItemPrice(item);
        const subtotal = qty * unitPrice;
        const isSelected = qty > 0;

        const cardBorder = isSelected
          ? 'border-2 border-wf-ink shadow-hard-emerald bg-wf-paper'
          : 'border-2 border-wf-ink shadow-hard-sm bg-white';

        const badgeStyle = item.badgeType === 'saffron'
          ? 'bg-wf-saffron text-wf-ink border border-wf-ink'
          : 'bg-white text-wf-ink border border-wf-ink';

        return `
          <div class="${cardBorder} p-5 flex flex-col justify-between transition-all">
            <div>
              <!-- Top SKU & Badge Row -->
              <div class="flex items-center justify-between gap-2 mb-4">
                <span class="font-mono text-[10px] text-neutral-500 uppercase tracking-wider">${item.sku}</span>
                <span class="font-mono text-[9px] font-extrabold px-2 py-0.5 uppercase tracking-wider ${badgeStyle}">
                  ${item.badge}
                </span>
              </div>

              <!-- Square SVG Icon + Item Name -->
              <div class="flex items-start gap-3.5 mb-5">
                <div class="w-12 h-12 border-2 border-wf-ink bg-wf-alabaster flex-shrink-0 flex items-center justify-center">
                  ${item.svg}
                </div>
                <div>
                  <h4 class="font-sans font-bold text-sm text-wf-ink leading-snug">
                    ${item.fullName}
                  </h4>
                  <div class="font-mono text-[11px] mt-1">
                    <span class="text-neutral-400 line-through mr-2">AVG: $${item.convPrice.toFixed(2)}</span>
                    <span class="text-wf-emerald font-extrabold">WF: $${unitPrice.toFixed(2)}</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Bottom Quantity Stepper Row -->
            <div class="pt-3 border-t border-neutral-300 flex items-center justify-between">
              <div class="font-mono text-[11px] font-bold uppercase ${isSelected ? 'text-wf-emerald' : 'text-neutral-400'}">
                ${isSelected ? `SUBTOTAL: $${subtotal.toFixed(2)}` : 'NOT IN RECEIPT'}
              </div>

              <div class="inline-flex border-2 border-wf-ink bg-white">
                <button onclick="updateQty('${item.id}', -1)" class="w-8 h-8 font-mono text-sm font-bold hover:bg-neutral-200 border-r-2 border-wf-ink flex items-center justify-center">
                  −
                </button>
                <span class="w-9 h-8 font-mono text-xs font-extrabold flex items-center justify-center ${isSelected ? 'bg-wf-emeraldLight text-wf-emerald' : 'bg-white text-wf-ink'}">
                  ${qty}
                </span>
                <button onclick="updateQty('${item.id}', 1)" class="w-8 h-8 font-mono text-sm font-bold hover:bg-wf-emerald hover:text-white border-l-2 border-wf-ink flex items-center justify-center">
                  +
                </button>
              </div>
            </div>
          </div>
        `;
      }).join('');

      // Calculate Live Receipt Totals
      let totalUnits = 0;
      let mythSum = 0;
      let convSum = 0;
      let wfSum = 0;
      let receiptRowsHtml = '';

      CATALOG.forEach(item => {
        const qty = basket[item.id] || 0;
        if (qty > 0) {
          const uPrice = getItemPrice(item);
          const lineMyth = item.mythPrice * qty;
          const lineConv = item.convPrice * qty;
          const lineWf = uPrice * qty;

          totalUnits += qty;
          mythSum += lineMyth;
          convSum += lineConv;
          wfSum += lineWf;

          receiptRowsHtml += `
            <div class="py-2.5 flex justify-between items-center">
              <div>
                <div class="font-bold text-wf-ink">${qty}x ${item.shortName}</div>
                <div class="text-[10px] text-neutral-500">${item.sku} @ $${uPrice.toFixed(2)}/ea</div>
              </div>
              <div class="flex items-center gap-6">
                <span class="text-neutral-400 line-through">$${lineConv.toFixed(2)}</span>
                <span class="font-extrabold text-wf-emerald text-sm">$${lineWf.toFixed(2)}</span>
              </div>
            </div>
          `;
        }
      });

      if (totalUnits === 0) {
        receiptRowsHtml = `
          <div class="py-8 text-center text-neutral-500">
            [ RECEIPT BASKET IS EMPTY — CLICK + ON ANY ITEM CARD ]
          </div>
        `;
      }

      const weeklySaved = Math.max(0, convSum - wfSum);
      const annualSaved = weeklySaved * 52;
      const ratioPct = convSum > 0 ? Math.min(100, Math.round((wfSum / convSum) * 100)) : 50;

      document.getElementById('active-unit-count').textContent = totalUnits;
      document.getElementById('nav-basket-badge').textContent = totalUnits;
      document.getElementById('receipt-myth-total').textContent = `$${mythSum.toFixed(2)}`;
      document.getElementById('receipt-conv-total').textContent = `$${convSum.toFixed(2)}`;
      document.getElementById('receipt-wf-total').textContent = `$${wfSum.toFixed(2)}`;
      document.getElementById('receipt-ratio-bar').style.width = `${ratioPct}%`;
      document.getElementById('receipt-line-items').innerHTML = receiptRowsHtml;
      document.getElementById('receipt-weekly-saved').textContent = `$${weeklySaved.toFixed(2)}`;
      document.getElementById('receipt-annual-saved').textContent = `$${annualSaved.toFixed(2)}/YR`;
    }

    function updateQty(itemId, delta) {
      const current = basket[itemId] || 0;
      const next = Math.max(0, current + delta);
      if (next === 0) {
        delete basket[itemId];
      } else {
        basket[itemId] = next;
      }
      renderCatalogAndReceipt();
    }

    function addItemToReceipt(itemId) {
      basket[itemId] = (basket[itemId] || 0) + 1;
      renderCatalogAndReceipt();
      const item = CATALOG.find(i => i.id === itemId);
      showToast(`ADDED 1x ${item.shortName.toUpperCase()} TO RECEIPT`);
    }

    function loadPreset(presetKey) {
      basket = { ...PRESETS[presetKey] };
      renderCatalogAndReceipt();
      showToast(`LOADED PRESET: ${presetKey.toUpperCase()}`);
    }

    function clearBasket() {
      basket = {};
      renderCatalogAndReceipt();
      showToast('CLEARED ALL RECEIPT ITEMS');
    }

    // =========================================================================
    // RENDER MODULE 03: $35 BUDGET MEAL ARCHITECT
    // =========================================================================
    function renderDietFilterBar() {
      const diets = ['ALL', 'HIGH-PROTEIN', 'VEGETARIAN'];
      const bar = document.getElementById('diet-filter-bar');
      bar.innerHTML = diets.map((d, idx) => {
        const isActive = activeDiet === d;
        const borderR = idx < diets.length - 1 ? 'border-r-2 border-wf-ink' : '';
        const bg = isActive ? 'bg-wf-ink text-white' : 'bg-white text-wf-ink hover:bg-wf-emeraldLight';
        return `
          <button onclick="setDiet('${d}')" class="px-3.5 py-2 font-mono text-xs font-bold uppercase ${borderR} ${bg}">
            ${d}
          </button>
        `;
      }).join('');
    }

    function setDiet(d) {
      activeDiet = d;
      renderDietFilterBar();
      renderMeals();
    }

    function setServings(s) {
      servingsScale = s;
      document.getElementById('scale-2-btn').className = s === 2
        ? 'px-4 py-2 font-mono text-xs font-bold uppercase bg-wf-emerald text-white border-r-2 border-wf-ink'
        : 'px-4 py-2 font-mono text-xs font-bold uppercase bg-white text-wf-ink border-r-2 border-wf-ink hover:bg-wf-emeraldLight';
      document.getElementById('scale-4-btn').className = s === 4
        ? 'px-4 py-2 font-mono text-xs font-bold uppercase bg-wf-emerald text-white'
        : 'px-4 py-2 font-mono text-xs font-bold uppercase bg-white text-wf-ink hover:bg-wf-emeraldLight';
      renderMeals();
    }

    function renderMeals() {
      const mult = servingsScale === 4 ? 2 : 1;
      const list = activeDiet === 'ALL' ? MEALS : MEALS.filter(m => m.diet === activeDiet);
      const grid = document.getElementById('meal-grid');

      grid.innerHTML = list.map(meal => {
        let wfTotal = 0;
        let convTotal = 0;

        const ingHtml = meal.items.map(entry => {
          const product = CATALOG.find(i => i.id === entry.id);
          const count = entry.qty * mult;
          const lineWf = getItemPrice(product) * count;
          const lineConv = product.convPrice * count;
          wfTotal += lineWf;
          convTotal += lineConv;

          return `
            <div class="py-2 flex items-center justify-between border-b border-neutral-200 font-mono text-xs">
              <div class="flex items-center gap-2">
                <div class="w-6 h-6 border border-wf-ink bg-wf-alabaster flex items-center justify-center">
                  ${product.svg}
                </div>
                <span class="text-wf-ink font-semibold">${count}x ${product.shortName}</span>
              </div>
              <span class="font-bold text-wf-emerald">$${lineWf.toFixed(2)}</span>
            </div>
          `;
        }).join('');

        const perPlate = wfTotal / servingsScale;

        return `
          <div class="border-2 border-wf-ink bg-white shadow-hard-sm p-6 flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between gap-2 mb-3">
                <span class="bg-wf-saffron border border-wf-ink px-2 py-0.5 font-mono text-[10px] font-extrabold uppercase">
                  ${meal.code} // ${meal.diet}
                </span>
                <span class="font-mono text-[10px] font-bold text-wf-emerald uppercase">
                  ${meal.time} • ${meal.protein}
                </span>
              </div>

              <h3 class="font-serif font-extrabold text-xl text-wf-ink leading-snug mb-4">
                ${meal.title}
              </h3>

              <div class="mb-5">
                ${ingHtml}
              </div>
            </div>

            <div>
              <div class="bg-wf-alabaster border-2 border-wf-ink p-3.5 mb-4 flex items-baseline justify-between">
                <div>
                  <div class="font-mono text-[10px] text-neutral-500 uppercase">TOTAL (${servingsScale} SERVINGS)</div>
                  <div class="font-serif font-extrabold text-2xl text-wf-emerald">
                    $${wfTotal.toFixed(2)}
                    <span class="font-mono text-xs text-neutral-400 line-through ml-1">$${convTotal.toFixed(2)}</span>
                  </div>
                </div>
                <div class="text-right">
                  <div class="font-mono text-[10px] text-neutral-500 uppercase">PER PLATE</div>
                  <div class="font-mono font-extrabold text-base text-wf-ink">$${perPlate.toFixed(2)}</div>
                </div>
              </div>

              <div class="grid grid-cols-2 gap-2.5">
                <button onclick="openRecipeModal('${meal.id}')" class="btn-rect bg-white hover:bg-wf-saffronLight text-wf-ink border-2 border-wf-ink py-2.5 px-3 font-mono text-[10px] font-bold uppercase tracking-wider">
                  [ VIEW STEPS ]
                </button>
                <button onclick="syncMealToReceipt('${meal.id}')" class="btn-rect bg-wf-emerald hover:bg-wf-emeraldDark text-white border-2 border-wf-ink py-2.5 px-3 font-mono text-[10px] font-bold uppercase tracking-wider">
                  [ + LOAD ITEMS ]
                </button>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    function syncMealToReceipt(mealId) {
      const meal = MEALS.find(m => m.id === mealId);
      const mult = servingsScale === 4 ? 2 : 1;
      meal.items.forEach(entry => {
        basket[entry.id] = (basket[entry.id] || 0) + (entry.qty * mult);
      });
      renderCatalogAndReceipt();
      showToast(`SYNCED ${meal.code} INGREDIENTS TO LIVE RECEIPT`);
    }

    function openRecipeModal(mealId) {
      const meal = MEALS.find(m => m.id === mealId);
      document.getElementById('modal-code').textContent = `${meal.code} // ${meal.diet} (${servingsScale} SERVINGS)`;
      document.getElementById('modal-title').textContent = meal.title;
      document.getElementById('modal-steps').innerHTML = meal.steps.map((s, i) => `
        <div class="p-3 border border-wf-ink bg-white font-sans">
          <span class="font-mono font-bold text-xs text-wf-emerald uppercase mr-2">STEP 0${i + 1}:</span>
          <span>${s}</span>
        </div>
      `).join('');
      const addBtn = document.getElementById('modal-add-btn');
      addBtn.onclick = () => {
        syncMealToReceipt(mealId);
        closeRecipeModal();
      };
      const modal = document.getElementById('recipe-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closeRecipeModal() {
      const modal = document.getElementById('recipe-modal');
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }

    // =========================================================================
    // GLOBAL PRIME MODE SWITCH & RECEIPT EXPORT
    // =========================================================================
    function togglePrimeMode() {
      primeMode = !primeMode;
      const indicator = document.getElementById('prime-square-indicator');
      const pill = document.getElementById('prime-discount-pill');
      const heroDelta = document.getElementById('hero-metric-delta');

      if (primeMode) {
        indicator.textContent = 'ON';
        indicator.className = 'w-8 h-8 border-2 border-wf-ink bg-wf-saffron flex items-center justify-center font-mono text-[11px] font-extrabold text-wf-ink shadow-hard-sm';
        pill.className = 'bg-wf-emerald text-white font-mono text-[9px] font-bold px-1 py-0.5';
        heroDelta.textContent = '-27.4%';
        showToast('PRIME RESET MODE: ON (EXTRA 10% MEMBER SAVINGS)');
      } else {
        indicator.textContent = 'OFF';
        indicator.className = 'w-8 h-8 border-2 border-wf-ink bg-neutral-200 flex items-center justify-center font-mono text-[11px] font-extrabold text-neutral-600';
        pill.className = 'bg-neutral-400 text-white font-mono text-[9px] font-bold px-1 py-0.5';
        heroDelta.textContent = '-19.8%';
        showToast('STANDARD 365™ EVERYDAY RESET PRICING ACTIVE');
      }

      renderMythbuster();
      renderCatalogAndReceipt();
      renderMeals();
    }

    function buildReceiptText() {
      let lines = [
        '============================================================',
        '              WHOLE FOODS MARKET — AUDIT LEDGER             ',
        '          HAVK WEB DEV COMPETITION // PULKIT TOMAR          ',
        '============================================================',
        `PRICING TIER: ${primeMode ? 'PRIME MEMBER RESET (-10% ACTIVE)' : '365 EVERYDAY RESET'}`,
        '------------------------------------------------------------'
      ];
      let convSum = 0;
      let wfSum = 0;

      CATALOG.forEach(item => {
        const qty = basket[item.id] || 0;
        if (qty > 0) {
          const u = getItemPrice(item);
          const lWf = u * qty;
          const lConv = item.convPrice * qty;
          convSum += lConv;
          wfSum += lWf;
          lines.push(`${qty}x ${item.fullName.padEnd(38, ' ')} WF: $${lWf.toFixed(2)} (Avg: $${lConv.toFixed(2)})`);
        }
      });

      const saved = Math.max(0, convSum - wfSum);
      lines.push('------------------------------------------------------------');
      lines.push(`CONVENTIONAL GROCER TOTAL:    $${convSum.toFixed(2)}`);
      lines.push(`WHOLE FOODS 2026 RESET TOTAL: $${wfSum.toFixed(2)}`);
      lines.push(`WEEKLY SAVINGS:               $${saved.toFixed(2)}`);
      lines.push(`52-WEEK ANNUALIZED SAVINGS:   $${(saved * 52).toFixed(2)}/YR`);
      lines.push('============================================================');
      return lines.join('\n');
    }

    function exportReceiptTxt() {
      const content = buildReceiptText();
      const blob = new Blob([content], { type: 'text/plain;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'WholeFoods-PriceReset-Receipt.txt';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      showToast('DOWNLOADED WholeFoods-PriceReset-Receipt.txt');
    }

    function copyReceiptSummary() {
      const content = buildReceiptText();
      navigator.clipboard.writeText(content).then(() => {
        showToast('COPIED RECEIPT AUDIT TO CLIPBOARD');
      });
    }

    function scrollToModule(id) {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    let toastTimer = null;
    function showToast(msg) {
      const box = document.getElementById('toast-box');
      const txt = document.getElementById('toast-text');
      txt.textContent = msg;
      box.classList.remove('hidden');
      if (toastTimer) clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        box.classList.add('hidden');
      }, 2600);
    }

    // Initialize All Modules on Load
    window.addEventListener('DOMContentLoaded', () => {
      renderMythbuster();
      renderCategoryTabs();
      renderCatalogAndReceipt();
      renderDietFilterBar();
      renderMeals();
    });
  </script>
</body>
</html>
"""

def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"[✓] Wrote illustrated competition site to: {out_path}")

    port = 8080
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    handler = http.server.SimpleHTTPRequestHandler

    # Try serving on localhost so all features work cleanly
    for p in range(8080, 8095):
        try:
            httpd = socketserver.TCPServer(("", p), handler)
            port = p
            break
        except OSError:
            continue
    else:
        webbrowser.open("file://" + out_path)
        return

    url = f"http://localhost:{port}/index.html"
    print(f"[✓] Launching Whole Foods — Price Image Reset at: {url}")
    print("    (Press Ctrl+C in the VS Code terminal to stop the server)")
    threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")

if __name__ == "__main__":
    main()
