# API 문서
## 개요
이 API는 Get 요청을 처리하며, "/hello" 엔드포인트 요청시 "Hello, World!" 라는 메시지를 반환합니다.

## 메소드
- `GET /hello`

## 엔드포인트
- /hello

## 세부 정보
### 1. GET /hello
- **설명**: Hello, World! 라는 메시지를 반환합니다.
- **파라미터**: 없음.
- **결과**: 
```json
 "Hello, World!"
```

### 응답 코드
- **200 OK** : 정상적으로 메시지를 반환했습니다.
- **404 Not Found** : 요청한 URI를 찾을 수 없습니다. URI를 확인해주세요.

## 스프링 컨트롤러 코드
```java
@RestController
public class HelloController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Hello, World!";
    }
}
```