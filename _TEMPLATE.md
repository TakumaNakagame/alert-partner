# {{ alert.annotations.title }}
## このAlertについて
{{ alert.annotations.wiki_about }}

### しきい値
{{ alert.annotations.wiki_threshold }}

## 緊急度
### {{ alert.labels.severity }}

## 影響
{{ alert.annotations.wiki_impact }}

## 対応すること
{{ alert.annotations.wiki_corresondence }}

## Alert Details
### expr
```
{{ alert.expr }}
```

### severity
```
{{ alert.labels.severity }}
```

### interval
```
{{ alert.for }}
```