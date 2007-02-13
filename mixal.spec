Summary:	Load-and-go assembler for Donald Knuth's MIX language
Summary(pl.UTF-8):	Asembler dla języka MIX Donalda Knutha
Name:		mixal
Version:	1.10
Release:	1
License:	distributable
Group:		Development/Languages
Source0:	http://www.catb.org/~esr/mixal/%{name}-%{version}.tar.gz
# Source0-md5:	7cd62ea97e6ae102b0f4926b88fc956b
URL:		http://www.catb.org/~esr/mixal/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mixal is an assembler and interpreter for Donald Knuth's mythical MIX
computer, defined in: Donald Knuth, "The Art of Computer Programming",
Vol. 1: Fundamental Algorithms_. Addison-Wesley, 1973 (2nd ed.)

%description -l pl.UTF-8
Mixal to asembler i interpreter dla mitycznego komputera MIX Donalda
Knutha, zdefiniowanego w pierwszej części "Fundamental Algorithms"
książki Donalda Knutha "The Art of Computer Programming", wydanej
przez Addison-Wesley w 1973 roku (drugie wydanie).

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

install mixal $RPM_BUILD_ROOT%{_bindir}/mixal
install mixal.1 $RPM_BUILD_ROOT%{_mandir}/man1/mixal.1
install *.mix $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MIX.DOC NOTES README
%attr(755,root,root) %{_bindir}/mixal
%{_mandir}/man1/*.1*
%{_examplesdir}/%{name}-%{version}
