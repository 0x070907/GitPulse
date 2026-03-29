# GitPulse

A GitHub profile analyzer that fetches your repos, events and stats,
scores your activity and generates a fully customized README.md —
ready to download and drop into your profile repo.

##  TODO

### Core Flow
- [ ] Search form — enter any GitHub username
- [ ] Loading page — 4-step animated progress indicator
- [ ] Fetch user + repos + events simultaneously 

### Analysis Dashboard
- [ ] Profile card — avatar, name, bio, location, member since, last active
- [ ] Stats row — repos, followers, following, total stars, total forks
- [ ] Profile strength progress bar — 0 to 100 with actionable tips
- [ ] Language breakdown — horizontal percentage bars with colour per language
- [ ] Repo quality score — top 3 repos with score badge
- [ ] All repos grid — All / Original only / Most starred filters
- [ ] Collaboration score badge — solo / building / active / contributor
- [ ] Activity insights — most active day, time, streak
- [ ] Recent activity feed — last 5 events timeline

### README Generator
- [ ] User input form — tech stack confirmation + optional fields
      (job/role, open to work, LinkedIn, Twitter/X, portfolio, fun fact, quote)
- [ ] generate_readme() — builds complete README.md string
- [ ] Construct URLs for typing animation, stats card, streak card, snake SVG
- [ ] Language + social badges via shields.io
- [ ] README preview + raw markdown — both panels visible, toggle switches between them
- [ ] Download as README.md 

### Polish
- [ ] Error pages — 404, 403, empty repos, network error
- [ ] Responsive layout — collapses to single column on mobile
- [ ] Deploy on Render
