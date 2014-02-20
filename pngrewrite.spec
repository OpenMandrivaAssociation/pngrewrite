Name:		pngrewrite
Version:	1.4.0
Release:	1
License:	BSD
Group:		Graphics
Source0:	%{name}-%{version}.tar.xz
URL:		http://entropymine.com/jason/pngrewrite/
Summary:	PNG size optimizer
BuildRequires:	pkgconfig(libpng)

%description
Pngrewrite is little utility that reduces the unnecessarily large
palettes that too many programs write into PNG files. It also
optimizes transparency settings, and reduces the bits-per-pixel
if possible. Handy for post-processing images before putting them
on a web site. 

%prep
%setup -q

%build
%make CFLAGS="%{optflags}"

%install
install -m755 %{name} -D %{buildroot}%{_bindir}/%{name}

%files
%doc readme.txt
%{_bindir}/%{name}
