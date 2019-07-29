# {{ alert.annotations.title }}
## このAlertについて
{{ alert.annotations.about }}

### しきい値
{{ alert.annotations.threshold }}

## 緊急度
### {{ alert.labels.severity }}

## 影響
{{ alert.annotations.impact }}

## 対応すること
{{ alert.annotations.corresondence }}

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